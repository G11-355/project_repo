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
    if current_user.is_authenticated:
        all_orders = filter_order_by_user(
            current_user.user_id, get_order_items())
        
        for order_id in all_orders:  # append the grand total cost to the end of each list in all_orders dict
            grand_total = sum([item[3] for item in all_orders[order_id]])
            all_orders[order_id].append(grand_total)
        
        return render_template('orderList.html', order_items=all_orders,
                               current_user=current_user)  # add template here
    else:
        flash('Please sign in to view your order history!')
        return redirect(url_for('login'))


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
'''


@app.route('/placeOrder/<int:current_order>', methods=['GET', 'POST'])
def place_order(current_order=0):
    items_by_type_dict = get_item_by_type()

    if current_user.is_authenticated:
        form = OrderTest()
        if current_order == 0:
            # get a temp order id to use if submitted
            order = make_new_order(current_user.user_id)
        else:
            order = Order.query.get(current_order)

        current_item_ids = [item[0] for item in get_order_item(order.order_id)]

        if form.validate_on_submit():
            return redirect(url_for('review_order', order_id=order.order_id))
        else:
            return render_template('order.html', form=form, items=items_by_type_dict,
                                   order=order, current_item_ids=current_item_ids)
    else:
        flash('Please sign in first!')
        return redirect(url_for('login'))

    # when access the order page an order id is generated for you
    # and if the order doesnt get places then we delete it from database
@app.route("/order/<int:item_id>/<int:order_id>/addToOrder", methods=['GET', 'POST'])
def add_item(item_id, order_id):
    item = Item.query.get(item_id)
    form = addToOrderForm()
    if form.validate_on_submit():
        q = form.quantity.data
        add_item_to_order(order_id=order_id, item_id=item_id, quanity=q)
        flash(f'{item.name} added to your order!')
        return redirect(url_for('place_order', current_order=order_id))
    return render_template('orderItem.html', form=form, item=item, order_id=order_id)


@app.route("/order/<int:item_id>/<int:order_id>/edit", methods=['GET', 'POST'])
def edit_item(item_id, order_id):
    # when access the order page an order id is generated for you
    # and if the order doesnt get places then we delete it from database
    item = Item.query.get(item_id)
    form = editToOrderForm()
    current_quant = get_quantity_item_in_order(order_id, item_id)
    if form.validate_on_submit():
        q = form.quantity.data
        if q == 0:
            print('Removing Item')
            remove_item_from_order(order_id, item_id)
        else:
            edit_item_quantity_in_order(order_id, item_id, q)
            print('edit to', q)
        return redirect(url_for('place_order', current_order=order_id))
    return render_template('editItem.html', form=form, item=item,
                           order_id=order_id, current_quant=current_quant)


@app.route("/review/<int:order_id>/", methods=['GET', 'POST'])
def review_order(order_id):
    form = reviewOrderForm()
    items, total_cost = get_order_items_and_total_price(order_id)
    total_items = get_total_items_in_order(order_id)
    if form.validate_on_submit():
        print(form.submit.data, form.edit.data, form.cancel.data)
        if form.submit.data:
            flash('Order has been submited. Thank you!')
            return redirect(url_for('list_order_items'))
        elif form.edit.data:
            print('Redirecting to place order!')
            return redirect(url_for('place_order', current_order=order_id))
        else:
            # wants to cancel order need to remove from database
            # since it has already been added
            remove_order(order_id)
            flash('Your order has been canceled!')
            return redirect(url_for('home'))

    return render_template('reviewOrder.html', items=items, form=form,
                           total_cost=total_cost, user=current_user,
                           total_items=total_items)


@app.route('/assign', methods=['GET', 'POST'])
def assign_staff():
    # user must be signed in and a manager
    if current_user.is_authenticated and current_user.user_id == current_user.manager_id:
        form = AssignStaffForm()
        ordering_customers = get_all_customers_who_have_ordered()
        if form.validate_on_submit():
            print('VALIDATED++++++++++++++++++++++++++++')
            assign_staff_to_order(form.staff_dropdown.data,
                                  form.order_dropdown.data)
            flash('Staff has been assigned to order')
            # add logic gor doing that here
            return redirect(url_for('home'))
        else:
            print('NOT VALIDATED++++++++++++++++')
            return render_template('assign.html', form=form,
                                   ordering_customers=ordering_customers)

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
        user = User(username=form.username.data, password=form.password.data,
                    address=form.address.data, phone_number=form.phone.data)
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
