from flask import render_template, session, redirect, url_for, flash
from . import applications

def check_session():
    if 'name' in session: #session exists and has key
        return session['name']
    else:
        return None

@applications.route('/apps', methods=['GET', 'POST'])
def application():
    session_var = check_session()
    return render_template('apps.html', user_profile=session_var)
