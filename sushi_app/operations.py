from datetime import datetime
from sushi_app.models import *
from random import choice
from sushi_app import db


def assign_order_contents(order_contents, username):
    order_ID = len(Order.query.all())
    date = datetime.now()
    date = f'{date.year}-{date.month}-{date.day}'
    
    users = User.query.all()
    cook = choice([user for user in users if user.specialty != None]).username
    order_contents = order_contents.split('\n')
    # add the new order
    new_order = Order(customer_username=username, staff_username=cook,
                      order_date=date)
    db.session.add(new_order)
    db.session.commit()
    
    
    for item in order_contents:
        item.strip()
        name, quantity = item.split(' ')
        