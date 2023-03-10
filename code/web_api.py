# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

'''
Access and retrieve data from Web API
'''

import urllib.request
import json


def get_ca_earthquake_data(day: str):
    '''
    Opens and reads the Earthquake API url based on
    the date that is given by the user.
    '''
    print('Opening and Reading Data....')
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&endtime=' + day  # noqa
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as res:
        res_data = res.read()
        api_data = json.loads(res_data)
        return api_data
