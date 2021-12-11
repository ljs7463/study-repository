from os import error
from flask import Blueprint, render_template, url_for, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from my_app import db

from my_app.forms import ChangePassword, UserCreateForm
from my_app.models.model import Users
# from my_app.models.model import Ingr, Pp_rp, In_rp, Raw_rp, Review, Users

from my_app.forms import UserCreateForm, UserLoginForm

import functools

bp = Blueprint('user', __name__, )

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if not user:
            user = Users(username = form.username.data,
                        password = generate_password_hash(form.password1.data),
                        user_id = form.username.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.main'))
        else:
            flash('User already existing')
    return render_template('signup.html', form=form)

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = Users.query.filter_by(username=form.username.data).first()
        if not user:
            error = "User does not exist"
        elif not check_password_hash(user.password, form.password.data):
            error = "Wrong password"
        if error is None:
            session.clear()
            session['user_name'] = user.username
            session['logged_in'] = True
            g.user = user
            return redirect(url_for('main.main')) 
        flash(error)
    return render_template('login.html', form=form)


@bp.before_app_request
def load_logged_in_user():
    user_name = session.get('user_name')

    if user_name == None:
        g.user = None
    else:
        g.user = db.session.query(Users).filter_by(username = user_name).first()
        # g.user = Users.query.get(user_name)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.main'))  




# breakpoint()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@bp.route('/my_page', methods=('GET', 'POST'))
def mypage():
    form = ChangePassword()

    if request.method == 'POST' and form.validate_on_submit():
        user = Users.query.filter_by(username = g.user.username).first()
        if g.user != user:
            flash('no authority')
            return redirect(url_for('user.mypage'))
    
        else:
            user.password = generate_password_hash(form.password.data)
            db.session.commit()
            render_template('my_page.html', form=form)

    return render_template('my_page.html', form=form)


@bp.route('/modify/<user_id>', methods=('GET', 'POST'))
@login_required
def modify(user_id):
    form = ChangePassword()

    user = Users.query.filter_by(username = user_id).first()
    
    if g.user != user:
        flash('no authority')
        return redirect(url_for('user.mypage'))
    
    else:
        user.password = generate_password_hash(form.password.data)
        db.session.commit()
        render_template('my_page.html', form=form)


@bp.route('/delete/<user_id>')
@login_required
def delete(user_id):
    user = Users.query.filter_by(username = user_id).first()
    if g.user != user:
        flash('no authority')
        return redirect(url_for('user.mypage'))
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('main.main'))