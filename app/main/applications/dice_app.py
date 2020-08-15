from flask import render_template, session, redirect, url_for, flash
from ..forms import NameFormDice
import random
from . import applications

def check_session():
    if 'name' in session: #session exists and has key
        return session['name']
    else:
        return None


# def dice_call():
#     dice_num = random.randint(1, 6)
#     return dice_num
    
@applications.route('/dice')
def dice():
    session_var = check_session()
    return render_template('dice.html', user_profile=session_var)