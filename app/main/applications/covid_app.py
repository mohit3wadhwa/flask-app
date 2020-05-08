from flask import render_template, session, redirect, url_for, flash
from ..forms import NameFormApps
import requests
from . import applications

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



@applications.route('/covid19-app', methods=['GET', 'POST'])
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
