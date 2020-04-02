from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FieldList, FormField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sushi_app.models import Item, User

# from CS needs to be modified for sushi
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('Address for Delivery', validators=[DataRequired()])
    phone = StringField('Callback Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AssignOrderForm():
    # want to list all open orders (no one assigned and then allow someone)
    # to add a server
    pass


class OrderForm(FlaskForm):
    choices = [(user.username, user.username)for user in User.query.all()]
    username = SelectField(label='Username: ', choices=choices)
    entry = TextAreaField(label='Enter Your Order Here', validators=[DataRequired()])
    submit = SubmitField('Submit Order')

class CustomForm(FlaskForm):
    pass


class EditMenuForm(FlaskForm):
    # form where a staff member can add update or delete menu items
    pass

class EditStaffForm(FlaskForm):
    # form where a manager on the staff can add or change or delete the
    # the staff members that they manage
    pass