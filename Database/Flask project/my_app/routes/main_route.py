from flask import Blueprint, render_template, request, session, g, url_for
from werkzeug.utils import redirect
from my_app import db
from my_app.models.model import item, sales, rating

bp = Blueprint('main', __name__)

@bp.route('/')


def main():
    #user_name = session.get('user_name')
    #test = db.session.query(item.title_orig).one()



    #return render_template('index.html'/, test = test)
    return render_template('index.html')