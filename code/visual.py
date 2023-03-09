# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

import matplotlib.pyplot as plt


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


def create_scatterplot(day, mag_lst, visualfile):
    x = range(len(mag_lst))
    plt.scatter(x, mag_lst)
    plt.xlabel(f'Number of Earthquake on {day}')
    plt.ylabel('Magnitude')
    plt.title(f"Scatter Plot of the Earthquake's Magnitudes on {day}")
    plt.savefig(visualfile)
