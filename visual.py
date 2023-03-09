# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

def sort_data(data):
    mag_list = []
    loc_list = []

    ind = 0
    while ind != len(data['features']):
        cali = data['features'][ind]['properties']['place']
        if 'CA' in str(cali):
            mag_list.append(data['features'][ind]['properties']['mag'])
            loc_list.append(cali)
        ind += 1
    return mag_list