# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

import webapi as WA
import visual
import json


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

    visual.sort_data(earthquake)