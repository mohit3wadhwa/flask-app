from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import NameFormSignUp
from .. import db
from ..models import User
from sqlalchemy import desc


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
            form.username.data = ''
            form.phone.data = ''
            form.email.data = ''
            return redirect(url_for('main.login'))
        
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
