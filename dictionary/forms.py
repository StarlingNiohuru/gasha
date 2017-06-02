from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired('username can not be blank'), Length(1, 20),
                                                   'username length must between 1-20'])
    password = PasswordField('password', validators=[DataRequired('password can not be blank'),
                                                     Length(6, 20, 'password length must between 6-20')])
