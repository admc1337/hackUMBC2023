from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class ZipCodeForm(FlaskForm):
    zipcode = IntegerField('ZipCode', 
                         validators=[Length(min=5,max=8)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Search Weather')

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[Length(min=2,max=20)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                             validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    