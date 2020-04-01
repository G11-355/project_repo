from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# from CS needs to be modified for sushi

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class OrderForm(FlaskForm):
    # form where a customer can place an order
    # if they do not have an account should have a way to redirect them
    # to the creat account form
    pass

class EditMenuForm(FlaskForm):
    # form where a staff member can add update or delete menu items
    pass

class EditStaffForm(FlaskForm):
    # form where a manager on the staff can add or change or delete the
    # the staff members that they manage
    pass