from flask import render_template, session, redirect, url_for, flash
from ..forms import NameFormZones
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import os
from . import applications

def check_session():
    if 'name' in session: #session exists and has key
        return session['name']
    else:
        return None


def zonedetails():
    url = 'https://api.covid19india.org/zones.json'
  
    try:
        list1 = []
        set_of_states = set()
        dictx = {}
        req = requests.get(url)
        print("Status Code: ",  req.status_code)
        res_dict = req.json()
        for value in res_dict.values():
            list1.append(value)
        list_of_dict = list1[0]
 
        for json in list_of_dict:
            set_of_states.add(json['state'])

        for item in set_of_states:
            for inner_item in list_of_dict:
                if item == inner_item['state']:
                    dictx[inner_item['statecode']] = item
                    break

        return set_of_states
    
    except ValueError:
        flash('Decoding JSON has failed. Problem with API Call')


def selected_dist_zone_details(state):

    dict_y = {}
    list1 = []

    orange_count = 0
    red_count = 0
    green_count = 0
    unknown_count = 0

    url = 'https://api.covid19india.org/zones.json'
  
    try:
        req = requests.get(url)
        print("Status Code: ",  req.status_code)
        res_dict = req.json()
        for value in res_dict.values():
            list1.append(value)
        list_of_dict = list1[0]
    
        for json in list_of_dict:
            if state == json['state']:
                #dict_y[json['district']] = json['zone']
                if json['zone'] == 'Orange':
                    orange_count += 1
                elif json['zone'] == 'Red':
                    red_count += 1
                elif json['zone'] == 'Green':
                    green_count += 1
                elif json['zone'] == '':
                    unknown_count +=1

            dict_y['orange']  = int(orange_count)
            dict_y['red']     = int(red_count)
            dict_y['green']   = int(green_count)
            dict_y['unknown'] = int(unknown_count)

        return dict_y

    except ValueError:
        flash('Decoding JSON has failed. Problem with API Call')


@applications.route('/states', methods=['GET', 'POST'])
def states():
    list1 = []
    list_x, list_y = [], []
    list1 = sorted(zonedetails())
    session_var = check_session()

    form = NameFormZones()
    form.states.choices = [(item, item) for item in list1]
    if form.validate_on_submit():
        all_zones_4_dist_list = selected_dist_zone_details(form.states.data)

        for key, value in all_zones_4_dist_list.items():
            list_x.append(key)
            list_y.append(value) 
        
        #my_stl = LS('#db290d', base_style=LCS) #red
        my_stl = LS('#43de14', base_style=LCS) #green
        #my_stl = LS('#ff8c00', base_style=LCS) #orange
        # my_stl = LS('#6e6464', base_style=LCS) #grey

        chart = pygal.Bar(style=my_stl, x_label_rotation=45, show_legend=False)
        chart.x_labels = list_x

        chart.add('', list_y)
        chart.render_to_file('app/static/images/graphs/' + form.states.data + '.svg')


        return render_template('zones.html', form=form, image_name='images/graphs/' + form.states.data + '.svg', user_profile=session_var)
    
    
    print(os.path)
    
    #os.remove(os.path.join(app.config['UPLOADED_ITEMS_DEST'],item.filename))
    return render_template('zones.html', form=form, image_name=None, user_profile=session_var)
    