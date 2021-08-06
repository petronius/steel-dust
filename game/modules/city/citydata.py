default_city_name_list = ['Samarqand', 'Cahokia', 'Boston', 'Xuu']

def get_random_city_name(namelist=default_city_name_list):
    if namelist is None or len(namelist) == 0:
        return "X"
    else:
        return namelist.pop()