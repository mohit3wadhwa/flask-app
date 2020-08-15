from flask import Blueprint
applications = Blueprint('applications', __name__)

from . import apps_dashboard, dice_app, covid_app, covid_India_app, tambola_app
