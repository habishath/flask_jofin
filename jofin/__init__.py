from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from os import path
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

    app.config['SECRET_KEY'] = "$ekr!tJHf#2$Zp%q7WBGr^&BxMN.tY9"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_name}"
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USER')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PWD')

    from .main.routes import main
    from .applicants.routes import applicant
    from .employers.routes import employer
    from .jobs.routes import jobs
    from .admin.routes import admin
    from .errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(applicant)
    app.register_blueprint(employer)
    app.register_blueprint(admin)
    app.register_blueprint(jobs)
    app.register_blueprint(errors) 

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    create_db(app)

    return app

def create_db(app):
    if not path.exists(f'{dir}/{db_name}'):
        with app.app_context():
            db.create_all()
