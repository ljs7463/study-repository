from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
    DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])

class ChangePassword(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired("New Password")])
    