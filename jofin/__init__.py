from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from os import path
from sqlalchemy import create_engine
from flask_mail import Mail

dir = 'jofin'
bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

db_name = 'jofin_db'
db_user = os.environ.get('DB_USER')
db_pwd = os.environ.get('DB_PWD')
secret_key = os.environ.get('SECRET_KEY')

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_name}"

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    create_db(app)

    return app

def create_db(app):
    if not path.exists(f'{dir}/{db_name}'):
        db.create_all(app=app)
