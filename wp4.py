# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

import webapi as WA
import visual
import json


if __name__ == "__main__":
    # date = input('Enter date (YYYY-MM-DD): ')
    # filename = input('Filename to save Earthquake Data: ')
    # visualname = input('Filename to save the graphical visual of the Earthquake Data: ')

    date = '2023-03-04'
    filename = 'quake'
    visualname = 'graph'

    earthquake = WA.get_CAearthquake_data(date)

    out_file = open(filename, 'w')
    json.dump(earthquake, out_file)
    out_file.close

    magnitude = visual.sort_data(earthquake)
    if len(magnitude) != 0:
        visual.create_scatterplot(date, magnitude, visualname)
    else:
        pass