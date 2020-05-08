from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_wtf import RecaptchaField
import os


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['RECAPTCHA_PUBLIC_KEY'] = RC_PUBLIC_KEY
    # app.config['RECAPTCHA_PRIVATE_KEY'] = RC_PRIVATE_KEY


    # app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    # @app.route('/hello/')
    # def hello():
    #     return 'Hello, Ji!'


    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .main.applications import applications as applications_blueprint
    app.register_blueprint(applications_blueprint)
    
    return app