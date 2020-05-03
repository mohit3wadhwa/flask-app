from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import NameFormApps, NameFormDice, NameFormTambola
from .. import db
from ..models import User
import requests
import random


def check_session():
    if 'name' in session: #session exists and has key
        return session['name']
    else:
        return None

def get_statics(country):
    url = "https://api.covid19api.com/summary"
    
    dict0, dict1 = {}, {}
    list1, list2 = [], []
    
    try:
        req = requests.get(url)
        print("Status Code: ",  req.status_code)
        res_dict = req.json()
        dict0 = res_dict['Global']
        list1 = res_dict['Countries']
    
        for items in range(0, len(list1) - 1):
            dict1 = list1[items]
            if dict1['Country'] == country:
                break
            dict1 = {}
    except ValueError:
        print('Decoding JSON has failed. Problem with API Call')
        
    if country == 'Global':
        list2.append(dict0['TotalConfirmed'])
        list2.append(dict0['TotalDeaths'])
        list2.append(dict0['TotalRecovered'])
    else:
        list2.append(dict1['TotalConfirmed'])
        list2.append(dict1['TotalDeaths'])
        list2.append(dict1['TotalRecovered'])
    
    return list2
    

@main.route('/apps', methods=['GET', 'POST'])
def apps():
    session_var = check_session()
    return render_template('apps.html', user_profile=session_var )


@main.route('/covid19-app', methods=['GET', 'POST'])
def covid19():
    session_var = check_session()
    country = None
    form = NameFormApps()
    if form.validate_on_submit():
        country = form.country.data
        list1 = []
        list1 = get_statics(country)
    
        return render_template('covid19.html', form=form, Country1=country, TotalConfirmed = list1[0], TotalDeaths = list1[1], TotalRecovered = list1[2], user_profile=session_var)

    return render_template('covid19.html', form=form, user_profile=session_var)


def dice_call():
    dice_num = random.randint(1, 6)
    return dice_num
    
@main.route('/dice', methods=['GET', 'POST'])
def dice():
    session_var = check_session()
    form = NameFormDice()
    if form.validate_on_submit():
        dice_num = dice_call()
        return render_template('dice.html', form=form, dice=str(dice_num), user_profile=session_var)
    
    return render_template('dice.html', form=form, dice='-', user_profile=session_var)

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
                        
            return render_template('tambola.html', form=form, numbers=list1, cut_num=cut_num_list[-1], cut_list=cut_num_list)
        else:
            listx = list(range(1, 91))
            cut_num_list = []
            list1 = [list(range(1, 11)), list(range(11, 21)), list(range(21, 31)), list(range(31, 41)), list(range(41, 51)),
                        list(range(51, 61)), list(range(61, 71)), list(range(71, 81)), list(range(81, 91))]
            
            return render_template('tambola.html', form=form, numbers=list1, cut_num='GAME OVER!')
   
    return render_template('tambola.html', form=form, numbers=list1, cut_list=cut_num_list, cut_num='Start')