from flask import render_template, url_for, flash, redirect, request
from sushi_app import app, db
from sushi_app.forms import *
from sushi_app.models import User, Item, OrderContents, Order
from sushi_app.models import Item
from flask_login import login_user, current_user, logout_user, login_required

#from flask_bcrypt import Bcrypt
#bcrypt = Bcrypt(app)

from sushi_app.operations import *
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

@app.route('/orderList')
def list_order_items():
        all_orders = get_order_items()
        print(all_orders, '\n\n\n')
        return render_template('orderList.html', order_items=all_orders)  # add template here
'''
@app.route('/order', methods=['GET', 'POST'])
def place_order():
    # DEPR USE ORDER
    if current_user.is_authenticated:
        form = OrderForm()
        if form.validate_on_submit():
            flash('Your order has been created!', 'success')
            assign_order_contents(form.entry.data, current_user.user_id)
            
            return redirect(url_for('home'))
        else:
            return render_template('order.html', form=form, current_user=f'{current_user.first_name} {current_user.last_name}')
    else:
        flash('Please sign in first!')
        return redirect(url_for('login'))
'''
@app.route("/orderList/<int:order_id>/update", methods=['GET', 'POST'])
def update_order(order_id):
    order = Order.query.get_or_404(order_id)
    form = EditOrderForm()
    form.delete_item.choices = get_order_item(order_id=order_id)
    if form.validate_on_submit():
        remove_item_from_order(order.order_id, form.delete_item.data)
        flash(f'Deleted item ID: {form.delete_item.data}')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        print('getting order item')
        form.delete_item.choices = get_order_item(order_id=order_id)
    return render_template('editOrder.html', form=form, order_id=order_id)


@app.route('/placeOrder/<int:current_order>', methods=['GET', 'POST'])
def place_order(current_order=0):
    if current_user.is_authenticated:
        form = OrderTest()
        if current_order == 0:
            order = make_new_order(current_user.user_id)  # get a temp order id to use if submitted
        else:
            order = Order.query.get(current_order)
        print('ORDERTEST ORDER', order.order_id)
        
        if form.validate_on_submit():
            flash('Order has been placed!')
            print(form.entry)
            return redirect(url_for('review_order', order_id=order.order_id))
        else:
            return render_template('order.html', form=form, items=Item.query.all(), order=order)
    else:
        flash('Please sign in first!')
        return redirect(url_for('login'))

@app.route("/order/<int:item_id>/<int:order_id>/addToOrder", methods=['GET', 'POST'])
def add_item(item_id, order_id):
    # when access the order page an order id is generated for you
    # and if the order doesnt get places then we delete it from database
    item = Item.query.get(item_id)
    form = addToOrderForm()
    if form.validate_on_submit():
        q = form.quantity.data
        print(order_id, 'CURRENT ORDER ID')
        add_item_to_order(order_id=order_id, item_id=item_id, quanity=q)
        flash(f'{item.name} added to your order!')
        return redirect(url_for('place_order', current_order=order_id))
    return render_template('orderItem.html', form=form, item=item, order_id=order_id)

@app.route("/review/<int:order_id>/", methods=['GET', 'POST'])
def review_order(order_id):
    items = get_order_items_and_total_price(order_id)
    print(items)

    return render_template('reviewOrder.html', items=items)
    
    
    
    
    
    

    
@app.route('/assign', methods=['GET', 'POST'])
def assign_staff():
    # user must be signed in and a manager
    if current_user.is_authenticated and current_user.user_id == current_user.manager_id:
        form = AssignStaffForm()
        if form.validate_on_submit():
            print('VALIDATED++++++++++++++++++++++++++++')
            assign_staff_to_order(form.staff_dropdown.data, form.order_dropdown.data)  
            flash('Staff has been assigned to order')
            # add logic gor doing that here
            return redirect(url_for('home'))
        else:
            print('NOT VALIDATED++++++++++++++++')
            return render_template('assign.html', form=form)
        
    flash('You must be a manager and signed in!')
    return redirect(url_for('login'))
    

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already signed in!')
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