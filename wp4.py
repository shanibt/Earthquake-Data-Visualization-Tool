# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

import webapi as WA
import visual
import fileIO

def main_ui():
    # Collect input from User
    date = input('Enter date (YYYY-MM-DD): ')
    filename = input('Filename to save Earthquake Data: ')
    visualname = input('Filename to save the graphical visual of the Earthquake Data: ')

    # Extract data from Earthquake API 
    earthquake = WA.get_CAearthquake_data(date)

    # Upload the data into a file
    fileIO.file_upload(earthquake, filename)

    # Get magnitude list of all the California Earthquakes on that day
    magnitude = visual.sort_data(earthquake)
    if len(magnitude) != 0:  #If there were earthquakes that day
        visual.create_scatterplot(date, magnitude, visualname)
        print('Visual created!')
    elif len(magnitude) == 0:  #If there were no earthquakes that day
        print('There were no earthquakes recorded on this day!')
        pass


if __name__ == "__main__":
    main_ui()
