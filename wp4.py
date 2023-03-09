# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

import webapi as WA
import json


if __name__ == "__main__":
    start_date = input('Enter start date (YYYY-MM-DD): ')
    end_date = input('Enter end date (YYYY-MM-DD): ')
    filename = input('Filename to save Earthquake Data: ')

    earthquake = WA.get_earthquake_data(start_date, end_date)

    out_file = open(filename, 'w')
    json.dump(earthquake, out_file)
    out_file.close