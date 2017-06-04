from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(1, 20, 'username length must between 1-20')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(6, 20, 'password length must between 6-20')])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[DataRequired(),
                                                         Length(6, 20, 'password length must between 6-20'),
                                                         EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[DataRequired()])
    submit = SubmitField('Update Password')

