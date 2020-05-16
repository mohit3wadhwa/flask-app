from flask import render_template, session, redirect, url_for, flash
from .forms import NameFormTambola
from .. import db
from ..models import User
import random
from . import main

def check_session():
    if 'name' in session: #session exists and has key
        return session['name']
    else:
        return None


listx = list(range(1, 91))
cut_num_list = []
list1 = [list(range(1, 11)), list(range(11, 21)), list(range(21, 31)), list(range(31, 41)), list(range(41, 51)),
             list(range(51, 61)), list(range(61, 71)), list(range(71, 81)), list(range(81, 91))]

def tambola_logic():
    rel_pos = random.randint(0, len(listx)-1)
    tambola_num = listx[rel_pos]
    listx.remove(tambola_num)
    return tambola_num

@main.route('/tambola', methods=['GET', 'POST'])
def tambola():
    global listx, cut_num_list, list1
    session_var = check_session()
    form = NameFormTambola()
    if form.validate_on_submit():
        if len(listx) > 0:
            cut_num_list.append(tambola_logic())
            i = 0
            for items in list1:
                j = 0
                for item in items:
                    for cut_nm in cut_num_list:
                        if item == cut_nm:
                            list1[i][j] = 0
                            break
                    j += 1
                i += 1
                        
            return render_template('tambola.html', form=form, numbers=list1, cut_num=cut_num_list[-1], cut_list=cut_num_list, user_profile=session_var)
        else:
            listx = list(range(1, 91))
            cut_num_list = []
            list1 = [list(range(1, 11)), list(range(11, 21)), list(range(21, 31)), list(range(31, 41)), list(range(41, 51)),
                        list(range(51, 61)), list(range(61, 71)), list(range(71, 81)), list(range(81, 91))]
            
            return render_template('tambola.html', form=form, numbers=list1, cut_num='GAME OVER!', user_profile=session_var)
   
    return render_template('tambola.html', form=form, numbers=list1, cut_list=cut_num_list, cut_num='Start', user_profile=session_var)
