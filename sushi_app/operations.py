from datetime import datetime
from sushi_app.models import *
from random import choice
from sushi_app import db


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
            new_order_contents = OrderContents(order_id=order_ID, item_id=item_id, quantity=quantity)
            db.session.add(new_order_contents)
            db.session.commit()



def assign_staff_to_order(user_id, order_id):
    order = Order.query.get_or_404(order_id)
    order.staff_id = user_id
    db.session.commit()


def get_order_items():
    # returns list of dictionaries order and the items in that order
    #order_items = db.session.query(Order, Item, OrderContents).join(Order).join(Item).join(OrderContents).filter(Order.order_id == OrderContents.order_id, Item.item_id == OrderContents.item_id).all()
    order_items = list(db.session.execute('SELECT ot.order_id, it.item_id, oct.quantity FROM order_tb as ot JOIN order_contents_tb as oct on ot.order_id = oct.order_id JOIN item_tb as it ON it.item_id = oct.item_id'))
    unique_orders = {}
    for order in order_items:
        if order[0] in unique_orders:
            unique_orders[order[0]].append([order[1], Item.query.filter_by(item_id=order[1]).first().name, order[-1]])
            # add the item name and the quantity ordered to list for that order id
        else:
            unique_orders[order[0]] = [[order[1], Item.query.filter_by(item_id=order[1]).first().name, order[-1]]]
    # {order_id: [[item, quanity], [item: quant]]}
    return unique_orders

def get_order_item(order_id):
    item_choices = []
    items_in_order = get_order_items()[order_id]
    for item in items_in_order:
        item_choices.append((item[0], item[1]))  # (itemid, itemname)
    return item_choices

def remove_item_from_order(order_id, item_id):
    order_contents = OrderContents.query.filter(OrderContents.order_id==order_id, OrderContents.item_id == item_id).first()
    db.session.delete(order_contents)
    db.session.commit()
    
    
    

    
        
    
    # join on 
    
    

        