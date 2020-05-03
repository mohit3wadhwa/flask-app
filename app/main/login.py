from datetime import datetime
from flask import render_template, session, redirect, url_for,flash
from . import main
from .forms import NameFormLogin
from .. import db
from ..models import User


@main.route('/login', methods=['GET', 'POST'])
def login():
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
            
    return render_template('login.html', form=form, user_profile=session.get('name'))
    #return render_template('login.html', form=form, name=name)
    
    # form = NameForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.name.data).first()
    #     if user is None:
    #         user = User(username = form.name.data)
    #         db.session.add(user)
    #         session['known'] = False
    #     else:
    #         session['known'] = True
    #     session['name'] = form.name.data
    #     form.name.data = ''
    #     return redirect(url_for('index'))
    #     #return render_template('login.html')
    # return render_template('login.html',
    #                         form = form, name = session.get('name'),
    #                         known = session.get('known', False),
    #                         current_time=datetime.utcnow())