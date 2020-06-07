from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .. import db
from ..models import User
import requests
from .forms import NameFormLogin


def get_statics():
    url = "https://api.adviceslip.com/advice"
    
    dict1 = {}
    req = requests.get(url)
    print("Status Code: ",  req.status_code)
    res_dict = req.json()
    dict1 = res_dict['slip']
    
    return dict1['advice']


@main.route('/', methods=['GET', 'POST'])
def index():
    #advice = get_statics()
    # if 'name' in session: #session exists and has key
    #     session_var = session['name']
    #     #return render_template('index.html', advice=advice, user_profile=session_var)
    #     return render_template('index.html', user_profile=session_var)
    # else: #session does not exist
    #     #return render_template('index.html', advice=advice)
    #     return render_template('index.html')
    
    form = NameFormLogin()
    if form.validate_on_submit():
        name = form.username.data
        password = form.password.data
        
        try:
            get_user = User.query.filter(User.username == name).first()
            if get_user == None:
                flash('You must signup first')
            else:
                get_user = User.query.filter(User.username == name).first()
            
                if not get_user.check_password(password):
                    flash('Password is not matching')
                else:
                    session['name'] = form.username.data
                    flash('Signing-in successful')
                    form.username.data = ''
                    return redirect(url_for('main.index'))
                
        except AssertionError as exception_message:
            flash(exception_message)
            
    return render_template('index.html', form=form, user_profile=session.get('name'))
    
    
@main.route('/signout')
def signout():
    session.pop('name')
    flash('You have been signed out successfully.')
    return redirect(url_for('main.index'))