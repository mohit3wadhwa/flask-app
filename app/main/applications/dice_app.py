from flask import render_template, session, redirect, url_for, flash
from ..forms import NameFormDice
import random
from . import applications

def check_session():
    if 'name' in session: #session exists and has key
        return session['name']
    else:
        return None


def dice_call():
    dice_num = random.randint(1, 6)
    return dice_num
    
@applications.route('/dice', methods=['GET', 'POST'])
def dice():
    session_var = check_session()
    form = NameFormDice()
    if form.validate_on_submit():
        dice_num = dice_call()
        return render_template('dice.html', form=form, dice=str(dice_num), user_profile=session_var)
    
    return render_template('dice.html', form=form, dice=None, user_profile=session_var)