from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import yaml

YAML_PATH = '/home/ethan/Documents/github/project_repo/sushi_app/db_linux.yaml'




# Configure db




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:782Judson@127.0.0.1/sushi'
app.config['SECRET_KEY'] = 'adsjfhkjh54jhk43jkashkjs3'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from sushi_app import routes
from sushi_app import models
models.db.create_all()
