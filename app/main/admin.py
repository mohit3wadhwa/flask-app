from datetime import date, timedelta
from flask import render_template, session, redirect, url_for, flash
from . import main
from .. import db
from ..models import User
import requests
from .forms import NameFormAdmin
import os

def check_session():
    if 'name' in session: #session exists and has key
        return session['name']
    else:
        return None

def get_users_details():
    dict_users = {}
    users_info = User.query.all()
    # print(f'users_info ', users_info)
    # print(f'type of users_info ', type(users_info))
    for item in users_info:
        dict_users[item.username] = str(item.email) + ',' + str(item.phone)
        # print(f'id:', item.id, f' username:', item.username)
    return dict_users

users_dict = {}
@main.route('/admin', methods=['GET', 'POST'])
def admin():
    global users_dict
    session_exists = check_session()
    if session_exists != None:
        if session_exists == os.environ.get('ADMIN_NAME'):
            return render_template('admin_users_list.html', user_info=users_dict, user_profile=session.get('name'))
        else:
            return redirect(url_for('main.index'))
    else:
        #tomo_date = date.today() + timedelta(days=1)
        form = NameFormAdmin()
        if form.validate_on_submit():
            name = form.username.data
            password = form.password.data
            if name != os.environ.get('ADMIN_NAME'):
                print(os.environ.get('ADMIN_NAME'))
                flash('You are not the Admin')
                return redirect(url_for('main.index'))
            try:
                #if str(tomo_date) != form.key.data:
                if form.key.data != os.environ.get('SECRET_KEY_ADMIN'):
                    flash('key is incorrect')
                    return redirect(url_for('main.index'))
                else:
                    get_user = User.query.filter(User.username == name).first()
                    if get_user == None:
                        flash('You must signup first')
                    else:
                        get_user = User.query.filter(User.username == name).first()
            
                        if not get_user.check_password(password):
                            flash('Password is not matching')
                        else:
                            session['name'] = form.username.data
                            form.username.data = ''
                            users_dict = get_users_details()
                            #return render_template('admin_dash.html', user_info=users_dict)
                            return render_template('admin_users_list.html', user_info=users_dict, user_profile=session.get('name'))
                    #return render_template('admin.html')
                
            except AssertionError as exception_message:
                flash(exception_message)
            
    return render_template('admin.html', form=form, user_profile=session.get('name'))
    
    
# @main.route('/signout')
# def signout():
#     session.pop('name')
#     flash('You have been signed out successfully.')
#     return redirect(url_for('main.index'))