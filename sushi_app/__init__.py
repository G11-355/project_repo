from flask import Flask
from sushi_app import routes
from sushi_app import models
from flask_sqlalchemy import SQLAlchemy
# from Flask.forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdkjf6l34jladjfl4jlad'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

models.db.create_all()