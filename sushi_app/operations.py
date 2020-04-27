from datetime import datetime
from sushi_app.models import *
from random import choice
from sushi_app import db


def get_order_id():
    '''
    Returns a valid order id that can be used for the current order.
    '''
    order_ids = Order.query.all()
    if order_ids:
        return sorted(order_ids, key=lambda x: x.order_id)[-1].order_id + 1
    else:
        return 1


def assign_order_contents(order_contents, customer_id):
    order_ID = len(Order.query.all()) + 1
    date = datetime.now()
    date = f'{date.year}-{date.month}-{date.day}'

    users = User.query.all()
    cook = choice([user for user in users if user.specialty != None]).user_id
    order_contents = order_contents.split('\n')
    # add the new order
    new_order = Order(order_id=order_ID, staff_id=cook,
                      order_date=date, customer_id=customer_id)
    db.session.add(new_order)
    db.session.commit()

    for items in order_contents:
        if items:
            item_id, quantity = items.split(' ')[0:2]
            item_id = item_id.strip()
            quantity = quantity.strip()
            new_order_contents = OrderContents(
                order_id=order_ID, item_id=item_id, quantity=quantity)
            db.session.add(new_order_contents)
            db.session.commit()


def assign_staff_to_order(user_id, order_id):
    order = Order.query.get_or_404(order_id)
    order.staff_id = user_id
    db.session.commit()


def get_order_items():
    # returns list of dictionaries order and the items in that order
    order_items = list(db.session.execute(
        'SELECT ot.order_id, it.item_id, it.description, it.cost, oct.quantity, \
            ot.order_date FROM order_tb as ot JOIN order_contents_tb as oct on \
            ot.order_id = oct.order_id JOIN item_tb as it ON \
            it.item_id = oct.item_id'))

    unique_orders = {}
    for order in order_items:

        item_details = [order[1], Item.query.filter_by(
            item_id=order[1]).first().name, order[2], order[3], order[4], order[5]]
        # [item_id, item_name, idescription, quantity, date]
        if order[0] in unique_orders:
            unique_orders[order[0]].append(item_details)
            # add the item name and the quantity ordered to list for that order id
        else:
            unique_orders[order[0]] = [item_details]
    # {order_id: [[item, quanity], [item: quant]]}
    return unique_orders


def filter_order_by_user(current_user_id, orders_dict):
    '''
    Filter orders that are shown. If user if is an employee return
    all orders in orders_dict. If not then return just the orders the
    current_user_id has placed.
    '''
    if User.query.get(current_user_id).manager_id:  # is an employee
        print(User.query.get(current_user_id).manager_id, 'manager id')
        return orders_dict  # allow to see all orders
    else:  # else filter orders by those customer has made
        customer_orders = {}
        for order in orders_dict:
            if Order.query.get(order).customer_id == current_user_id:
                customer_orders[order] = orders_dict[order]
        print(customer_orders)
        return customer_orders


def get_order_item(order_id):
    all_item_orders = get_order_items()
    if order_id in all_item_orders:
        return all_item_orders[order_id]
    else:
        return []


def get_all_customers_who_have_ordered():
    '''
    returns the user_id, firstname and lastname of all customers who have
    made an order.
    '''
    customers = list(db.session.execute(
        'SELECT user_tb.user_id, user_tb.first_name, user_tb.last_name FROM \
            user_tb where user_tb.user_id IN (SELECT order_tb.customer_id \
                FROM order_tb)'
    ))
    return customers


def get_order_items_and_total_price(order_id):
    items_ordered = get_order_items()[order_id]
    item_name_quant_cost = []
    grand_total = 0
    for item in items_ordered:
        cost = Item.query.get(item[0]).cost
        print(cost, item[4])
        item_name_quant_cost.append([item[0], item[1], item[4],
                                     cost, item[4] * cost])
        grand_total += item[4] * cost
    return item_name_quant_cost, grand_total


def get_quantity_item_in_order(order_id, item_id):
    '''
    Given an order_id and the item number returns the quantity of that
    item in that order as an integer.
    '''
    q = db.session.execute(f'SELECT order_contents_tb.quantity \
        FROM order_contents_tb WHERE order_contents_tb.order_id = {order_id} \
        AND order_contents_tb.item_id = {item_id}')
    if not q:
        q = 0
    else:
        q = q.first()[0]

    return q


def get_total_items_in_order(order_id):
    '''
    Get total number of different types of items in order
    '''
    q = db.session.execute(f' SELECT COUNT(*)  AS "total_items" FROM order_contents_tb \
        WHERE order_contents_tb.order_id = {order_id}')
    if not q:
        q = 0
    else:
        q = q.first()[0]
    print(q, 'total items', type(q))
    return q


def edit_item_quantity_in_order(order_id, item_id, new_quantity):
    OrderContents.query.filter_by(
        order_id=order_id, item_id=item_id).update({'quantity': new_quantity})
    #order_contents.quanity = new_quantity
    #order_contents
    db.session.commit()


def get_item_by_type():
    '''
    Returns a dictionary of items where the key is the item type. If the key is
    in the TRANS_DICT it will return the value of that key in the trans_dict.
    '''
    TRANS_DICT = {'app': 'Appetizers', 'sal': 'Salads', 'sop': 'Soups',
                  'ent': 'Entrees', 'drk': 'Drinks'}
    item_dict = {}
    for item in Item.query.all():
        if item.type in item_dict:
            item_dict[item.type].append(item)
        else:
            item_dict[item.type] = [item]
    item_dict = {TRANS_DICT[t]: item_dict[t]
                 for t in item_dict if t in TRANS_DICT}

    return item_dict


def remove_item_from_order(order_id, item_id):
    order_contents = OrderContents.query.filter_by(order_id=order_id,
                                                   item_id=item_id).first()

    db.session.delete(order_contents)
    db.session.commit()


def add_item_to_order(order_id, item_id, quanity):
    new_content = OrderContents(order_id=order_id, item_id=item_id,
                                quantity=quanity)
    db.session.add(new_content)
    db.session.commit()


def get_current_datetime():
    '''
    Returns the datetime at the time of the function call.
    '''
    date = datetime.now()
    return f'{date.year}-{date.month}-{date.day}'


def make_new_order(customer_id, staff_id=None):
    '''
    Makes a new order based on the given customer_id. If staff id is left as 
    none then randomly assigns a staff member to the order. Queries the Order
    table to get an allowed order_id.
    '''
    order_id = get_order_id()
    if staff_id == None:  # if staff id not given assign random staff
        users = User.query.all()
        staff_id = choice(
            [user for user in users if user.specialty != None]).user_id

    order = Order(order_id=order_id, customer_id=customer_id,
                  staff_id=staff_id, order_date=get_current_datetime())

    session_add_commit(order)

    return order


def remove_order(order_id):
    '''
    Remove all entries in the ordercontents table with a given order id. Then
    remove that order with the order_id from the order table.
    '''
    if Order.query.get(order_id):  # if a valid order
        contents = OrderContents.query.filter_by(order_id=order_id)
        order = Order.query.get(order_id)
        for con in contents:
            db.session.delete(con)
        db.session.commit()

        db.session.delete(order)
        db.session.commit()


def get_order_contents(order_id, item_id):
    '''
    Given an order id and the item id returns an order contents object if it
    exists
    '''
    return OrderContents.query.filter(OrderContents.order_id == order_id, OrderContents.item_id == item_id)

    # join on


def session_add_commit(thing_to_add):
    db.session.add(thing_to_add)
    db.session.commit()
