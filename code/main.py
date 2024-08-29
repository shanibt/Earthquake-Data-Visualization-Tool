'''
Launches the main.py to collect input from User to extract data
from an earthquake API and produce a scatter plot based on the
magnitudes of the earthquakes on the given date
'''

import web_api as WA
import visual
import file_io
import data_checker


def main_ui():
    '''
    Main User Interface
    Collects the input from user and checks to make sure the
    date given is valid. Use the input to extract data from
    the Earthquake API and upload the data into a file, under
    the given file name. From the data extracted from the
    Earthquake API, check and add the magnitudes of earthquakes
    that happened in California on the date given.
    '''
    # Collect input from user
    date = input('Enter date (YYYY-MM-DD): ')
    if not data_checker.check_date(date):
        print('Error: Invalid Date -- Rerun the program if you wish')
        exit(1)
    filename = input('Filename to save Earthquake Data: ')
    visualname = input('Filename to save the graphical '
                       'visual of the Earthquake Data: ')

    # Extract data from Earthquake API
    earthquake = WA.get_ca_earthquake_data(date)

    # Upload the data into a file
    file_io.file_upload(earthquake, filename)

    # Get magnitude list of all the California Earthquakes on that day
    magnitude = visual.sort_data(earthquake)
    if len(magnitude) != 0:  # If there were earthquakes that day
        visual.create_scatterplot(date, magnitude, visualname)
        print('Visual created!')
    elif len(magnitude) == 0:  # If there were no earthquakes that day
        print('There were no earthquakes in California recorded on this day!')


if __name__ == "__main__":
    main_ui()
