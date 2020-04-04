from datetime import datetime
from flaskDemo import db, login_manager
from flask_login import UserMixin
from functools import partial
from sqlalchemy import orm

db.Model.metadata.reflect(db.engine)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
     __table_args__ = {'extend_existing': True}
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(100), nullable=False)
     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
     content = db.Column(db.Text, nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

     def __repr__(self):
         return f"Post('{self.title}', '{self.date_posted}')"






class Dependent(db.Model):
    __table__ = db.Model.metadata.tables['dependent']
    
class Department(db.Model):
    __table__ = db.Model.metadata.tables['department']

# used for query_factory
def getDepartment(columns=None):
    u = Department.query
    if columns:
        u = u.options(orm.load_only(*columns))
    return u

def getDepartmentFactory(columns=None):
    return partial(getDepartment, columns=columns)

class Dept_Locations(db.Model):
    __table__ = db.Model.metadata.tables['dept_locations']
    
class Employee(db.Model):
    __table__ = db.Model.metadata.tables['employee']
class Project(db.Model):
    __table__ = db.Model.metadata.tables['project']
class Works_On(db.Model):
    __table__ = db.Model.metadata.tables['works_on']

    

  
