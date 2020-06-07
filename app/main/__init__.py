from flask import Blueprint

main = Blueprint('main', __name__)

<<<<<<< HEAD
from . import home, errors, signup, admin, login
=======
from . import home, login, errors, signup, tambola
>>>>>>> 92e10fb7a572491c3e52a147c6275b2fb194599c
from ..models import Permission

# from .apps import apps as apps_blueprint
# app.register_blueprint(apps_blueprint)

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
