from flask import Blueprint

main = Blueprint('main', __name__)

from . import home, login, errors, signup, tambola, admin
from ..models import Permission

# from .apps import apps as apps_blueprint
# app.register_blueprint(apps_blueprint)

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
