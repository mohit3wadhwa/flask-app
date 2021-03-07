from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, send_file
from . import main
from .. import db
from ..models import User
import requests
from .forms import NameFormLogin


def get_advice():
    url = "https://api.adviceslip.com/advice"
    
    dict1 = {}
    req = requests.get(url)
    print("Status Code: ",  req.status_code)
    res_dict = req.json()
    dict1 = res_dict['slip']
    
    return dict1['advice']

def get_covid_stat():
    url = "https://api.covid19api.com/summary"
    
    dictCov = {}
    list1, listCov = [], []
    
    try:
        req = requests.get(url)
        print("Status Code: ",  req.status_code)
        res_dict = req.json()
        list1 = res_dict['Countries']
    
        for items in range(0, len(list1) - 1):
            dictCov = list1[items]
            if dictCov['Country'] == "India":
                break
            dictCov = {}
    except ValueError:
        print('Decoding JSON has failed. Problem with API Call')

    listLab = []
    listLab.append('Total Confirmed Cases')
    listLab.append('Total Recovered Cases')
    listLab.append('Total Deaths')
    
    listCov.append(dictCov['TotalConfirmed'])
    listCov.append(dictCov['TotalRecovered'])
    listCov.append(dictCov['TotalDeaths'])
    
    
    return listLab, listCov


@main.route('/', methods=['GET', 'POST'])
def index():
    #advice = get_statics()
    # if 'name' in session: #session exists and has key
    #     session_var = session['name']
    #     #return render_template('index.html', advice=advice, user_profile=session_var)
    #     return render_template('index.html', user_profile=session_var)
    # else: #session does not exist
    #     #return render_template('index.html', advice=advice)
    #     return render_template('index.html')

    
    #bar_labels, bar_values = get_covid_stat()
    bar_labels, bar_values = [], []
    
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
            
    return render_template('index.html', user_profile=session.get('name'), title='Covid Statistics for India', max=17000, labels=bar_labels, values=bar_values)
    
    
@main.route('/downloads')
def downloads():
    return send_file('static/downloads/Mohit_Profile.pdf', attachment_filename='Mohit_profile.pdf')
#/Users/mohitwadhwa/Desktop/Techy/github/app/static/downloads/Mohit_Profile.pdf
@main.route('/signout')
def signout():
    session.pop('name')
    flash('You have been signed out successfully.')
    return redirect(url_for('main.index'))
