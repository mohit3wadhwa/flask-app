from flask import render_template, session, redirect, url_for, flash
from .forms import NameFormTambola
from .. import db
from ..models import User
import random
from . import main

def check_user_session():
    if 'name' in session:
        return session['name']
    else:
        return None

def check_game_session():
    if not 'tambola' in session:
        session['tambola'] = 'Game ON'
        session['listx_s'] = list(range(1, 91))
        session['cut_num_list_s'] = []
        session['list1_s'] = [list(range(1, 11)), list(range(11, 21)), list(range(21, 31)), list(range(31, 41)), list(range(41, 51)),
             list(range(51, 61)), list(range(61, 71)), list(range(71, 81)), list(range(81, 91))]

def tambola_logic():
    #listx_s = session['listx_s']
    # rel_pos = random.randint(0, len(listx_s)-1)
    # tambola_num = listx_s[rel_pos]
    # listx_s.remove(tambola_num)

    rel_pos = random.randint(0, len(session['listx_s'])-1)
    tambola_num = session['listx_s'][rel_pos]
    #print(f'relative pos: ', rel_pos, f' actual num: ', tambola_num)
    session['listx_s'].remove(tambola_num)
    session.modified = True
    #session['listx_s'] = listx_s
    return tambola_num

@main.route('/tambola', methods=['GET', 'POST'])
def tambola():
    #global listx, cut_num_list, list1
    user_name = check_user_session()
    check_game_session()

    # print(session['listx_s'])
    # print(session['cut_num_list_s'])
    # print(session['list1_s'])

    form = NameFormTambola()
    if form.validate_on_submit():
        if len(session['listx_s']) > 0:
            session['cut_num_list_s'].append(tambola_logic())
            session.modified = True
            i = 0
            for items in session['list1_s']:
                j = 0
                for item in items:
                    for cut_nm in session['cut_num_list_s']:
                        if item == cut_nm:
                            session['list1_s'][i][j] = 0
                            session.modified = True
                            break
                    j += 1
                i += 1
                        
            return render_template('tambola.html', form=form, numbers=session['list1_s'], cut_num=session['cut_num_list_s'][-1], cut_list=session['cut_num_list_s'], user_profile=user_name)
        else:
            session.pop('tambola')
            check_game_session()
            # listx = list(range(1, 91))
            # cut_num_list = []
            # list1 = [list(range(1, 11)), list(range(11, 21)), list(range(21, 31)), list(range(31, 41)), list(range(41, 51)),
            #             list(range(51, 61)), list(range(61, 71)), list(range(71, 81)), list(range(81, 91))]
            
            return render_template('tambola.html', form=form, numbers=session['list1_s'], cut_num='GAME OVER!', user_profile=user_name)
   
    return render_template('tambola.html', form=form, numbers=session['list1_s'], cut_list=session['cut_num_list_s'], cut_num='Start', user_profile=user_name)
