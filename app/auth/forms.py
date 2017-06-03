from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20, 'username length must between 1-20')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(6, 20, 'password length must between 6-20')])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
