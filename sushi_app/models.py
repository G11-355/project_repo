from sushi_app import db
from sushi_app import login_manager
from flask_login import UserMixin


# reflect the tables currently in the database
db.Model.metadata.reflect(db.engine)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __table__=db.Model.metadata.tables['user_tb']
    def get_id(self):
           return (self.user_id)

class Item(db.Model):
    __table__=db.Model.metadata.tables['item_tb']
    
class Order(db.Model):
    __table__=db.Model.metadata.tables['order_tb']

class OrderContents(db.Model):
    __table__=db.Model.metadata.tables['order_contents_tb']
