from flask import render_template, url_for, flash, redirect, request
from sushi_app import app, db
from sushi_app.forms import *
from sushi_app.models import User, Item, OrderContents, Order
from sushi_app.models import Item
from flask_login import login_user, current_user, logout_user, login_required

#from flask_bcrypt import Bcrypt
#bcrypt = Bcrypt(app)

from sushi_app.operations import assign_order_contents
#from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]
# just for testing



@app.route("/", methods=['GET', 'POST'])
@app.route("/home")
def home():
    items = Item.query.all()
    return render_template('home.html', items=items)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/order', methods=['GET', 'POST'])
def place_order():
    '''
    items = Item.query.all()
    item_dict = []
    for item in items:
        item_dict.append({'quantity': 0})
    
    form = OrderForm(items=item_dict)
    return render_template('order.html', form=form)
    '''
    if current_user.is_authenticated:
        form = OrderForm()
        if form.validate_on_submit():
            flash('Your order has been created!', 'success')
            assign_order_contents(form.entry.data, current_user.username)
            
            return redirect(url_for('home'))
        else:
            return render_template('order.html', form=form, current_user=current_user.username)
    else:
        flash('Please sign in first!')
        return redirect(url_for('login'))
    

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
       # hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,password=form.password.data, address=form.address.data, phone_number=form.phone.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and form.password.data == user.password:
            login_user(user)
            next_page = request.args.get('next')
            flash('You have been logged in!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)