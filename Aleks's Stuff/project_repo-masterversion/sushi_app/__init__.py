from flask import Flask
import os, sys
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

ENV = 'mysql://student:student@localhost/projectdb2'

app = Flask(__name__)

# change this URI based on your password / operating system needs
# or set an environmental variable named SQL_URI to your connection
# string

if os.getenv(ENV):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(ENV)
else:  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://student:student@localhost/projectdb2'

if app.config['SQLALCHEMY_DATABASE_URI'] == 'YOUR_URI_HERE':
    print('STOP IN THE NAME OF THE LAW!!')
    print('YOU HAVE NOT SET YOUR URI IN THE __INIT__.py FILE!!!')
    sys.exit()
    
    
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from sushi_app import routes
from sushi_app import models
models.db.create_all()
