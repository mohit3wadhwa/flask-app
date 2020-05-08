import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

def get_zone_details():
    url = 'https://api.covid19india.org/zones.json'
  
    try:
        list1 = []
        set_of_states = set()
        req = requests.get(url)
        print("Status Code: ",  req.status_code)
        res_dict = req.json()
        for value in res_dict.values():
            list1.append(value)
        list_of_dict = list1[0]
 
        for json in list_of_dict:
            set_of_states.add(json['state'])


        orange_count = 0
        red_count = 0
        green_count = 0
        unknown_count = 0
        dict_final = {}

        for state in set_of_states:
            for json in list_of_dict:
                if state == json['state']:
                    if json['zone'] == 'Orange':
                        orange_count += 1
                    elif json['zone'] == 'Red':
                        red_count += 1
                    elif json['zone'] == 'Green':
                        green_count += 1
                    elif json['zone'] == '':
                        unknown_count +=1
            dict_final[state] = str(orange_count) + ' ' + str(red_count) + ' ' + str(green_count) + ' ' + str(unknown_count)
            orange_count = 0
            red_count = 0
            green_count = 0
            unknown_count = 0

        return dict_final
    
    except ValueError:
        print('Decoding JSON has failed. Problem with API Call')

list_dist, list_orange, list_red, list_green, list_unkn = [], [], [], [], []
var_orange, var_red, var_green, var_unkn = 0, 0, 0, 0

dict0 = get_zone_details()

for key, value in dict0.items():
    list_dist.append(key)
    var_orange, var_red, var_green, var_unkn = value.split()
    list_orange.append(int(var_orange))
    list_red.append(int(var_red))
    list_green.append(int(var_green))
    list_unkn.append(int(var_unkn))

print(list_dist)
print(list_orange)
print(list_red)
print(list_green)
print(list_unkn)
print(dict0)

#my_stl = LS('#db290d', base_style=LCS) #red
my_stl = LS('#43de14', base_style=LCS) #green
#my_stl = LS('#ff8c00', base_style=LCS) #orange
# my_stl = LS('#6e6464', base_style=LCS) #grey

chart = pygal.Bar(style=my_stl, x_label_rotation=45, show_legend=False)
chart.x_labels = list_dist

chart.add('', list_green)
chart.render_to_file('python_covid19.svg')

