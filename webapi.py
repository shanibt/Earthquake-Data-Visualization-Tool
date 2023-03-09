# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

import urllib.request
import json

def get_earthquake_data(start:str, end:str):
    print('Opening and Reading Data....')
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=' + start + '&endtime=' + end
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    res_data = res.read()
    res.close()
    api_data = json.loads(res_data)
    print('Done!')
    return api_data
