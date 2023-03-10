# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

'''
Sort the extracted data for only California magnitudes and
create and save the scatterplot that depicts the varying
magnitudes of the earthquakes on the given date.
'''

import matplotlib.pyplot as plt


def sort_data(data):
    '''
    Sort the data extracted from the Earthquake API to
    create 2 lists. One for all the earthquake's magnitudes
    on the given date and the other for all the California
    location of these earthquakes.
    '''
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


def create_scatterplot(day, mag_lst, visualfile):
    '''
    Create a scatterplot for California's Earthquake Magnitude
    on the date given by the user.
    '''
    x_axis = range(len(mag_lst))
    plt.scatter(x_axis, mag_lst)
    plt.xlabel(f'Number of Earthquake on {day}')
    plt.ylabel('Magnitude')
    plt.title(f"Scatter Plot of the Earthquake's Magnitudes on {day}")
    plt.savefig(visualfile)
