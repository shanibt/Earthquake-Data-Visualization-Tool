# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

import webapi as WA
import json

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



if __name__ == "__main__":
    # start_date = input('Enter start date (YYYY-MM-DD): ')
    # end_date = input('Enter end date (YYYY-MM-DD): ')
    # filename = input('Filename to save Earthquake Data: ')
    # visualname = input('Filename to save the graphical visual of the Earthquake Data: ')

    start_date = '2023-01-09'
    end_date = '2023-01-10'
    filename = 'quake'

    earthquake = WA.get_CAearthquake_data(start_date, end_date)

    out_file = open(filename, 'w')
    json.dump(earthquake, out_file)
    out_file.close

    sort_data(earthquake)