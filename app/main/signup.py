from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import NameFormSignUp
from .. import db
from ..models import User
from sqlalchemy import desc
import requests
import json
import os

def pust_to_slack(user_name):
    web_hook_url = os.environ.get('WEB_HOOK_URL_SLACK')
    slack_msg = {'text': user_name + ' has signed up!'}
    requests.post(web_hook_url, data=json.dumps(slack_msg))


@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = NameFormSignUp()
    if form.validate_on_submit():
        #get_id = User.query.order_by(desc(User.id)).first()
        try:
            user = User(username=form.username.data, email=form.email.data, phone=form.phone.data)
            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()
            flash('Sign-up is completed, you should log in now!')
            pust_to_slack(form.username.data)

            form.username.data = ''
            form.phone.data = ''
            form.email.data = ''
            return redirect(url_for('main.index'))
        
        except AssertionError as exception_message:
            flash(exception_message)
        
    return render_template('signup.html', form=form)


        
        # if get_id == None:
        #     item = User(id=1,
        #             username=form.name.data,
        #             phone=form.phone.data,
        #             email=form.email.data,
        #             password_hash=form.password.data
        #             )
        # else:
        #     print(get_id.id)
        #     new_id = get_id.id + 1
        #     item = User(id=new_id,
        #             username=form.name.data,
        #             phone=form.phone.data,
        #             email=form.email.data,
        #             password_hash=form.password.data
        #             )
