from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FieldList, FormField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sushi_app.models import Item, User, Order
from sushi_app import db

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

class AssignStaffForm(FlaskForm):
    # get join of all customers and orders
    customer_orders = db.session.query(Order, User).join(Order, User.user_id == Order.customer_id).all()
    users = User.query.all()
    customers, staff = [], []
    for co in customer_orders:
        customers.append((co[0].order_id, f'{co[1].username} {co[0].order_date}'))
    print(customers, '*******************************************')
        # set up order choices based on customers who have made orders
    for s in users:
        if s.manager_id:
            staff.append((s.user_id, f'{s.first_name} {s.last_name}'))

    
    order_dropdown = SelectField(label='Select Orders', 
                                  choices=customers, validators=[DataRequired()], coerce=int)
    staff_dropdown = SelectField(label='Select Staff', 
                                 choices=staff, validators=[DataRequired()], coerce=int)
    
    submit = SubmitField('Submit Assignment')
    

class OrderForm(FlaskForm):
    entry = TextAreaField(label='Enter Your Order Here', validators=[DataRequired()])
    submit = SubmitField('Submit Order')

class EditOrderForm(FlaskForm):
    delete_item = SelectField(label='Select Item to Delete', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Delete')


class OrderTest(FlaskForm):
    entry = IntegerField(label='Quantity', default=0)
    submit = SubmitField(label='Submit Order')


class addToOrderForm(FlaskForm):
    quantity = IntegerField(label='Quantity', default=1)
    submit = SubmitField(label='Add Item')

class reviewOrderForm(FlaskForm):
    submit = SubmitField(label='Complete Order')
    cancel = SubmitField(label='Cancel Order')
    edit = SubmitField(label='Edit Order')