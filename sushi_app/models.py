from sushi_app import db


db.Model.metadata.reflect(db.engine)

class User(db.model):
    __table__=db.Model.metadata.tables['user_tb']

class Item(db.model):
    __table__=db.Model.metadata.tables['item_tb']

class OrderContents(db.model):
    __table__=db.Model.metadata.tables['item_tb']

class Order(db.model):
    __table__=db.Model.metadata.tables['item_tb']
