# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

import urllib.request
import json

def get_earthquake_data(start, end) -> dict:
    url_name = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=' + start + '&endtime=' + end
    req = urllib.request.Request(url_name)
    res = urllib.request.urlopen(req)
    res_data = res.read()
    res.close()
    api_obj = json.loads(res_data)
    return api_obj

#magnitude, 
# start_date: str, end_date: str, apikey

if __name__ == "__main__":
    filename = 'quake'
    start_date = "2023-03-01"
    end_date = "2023-03-09"
    earthquake = get_earthquake_data(start_date, end_date)

    out_file = open(filename, 'w')
    json.dump(earthquake, out_file)
    out_file.close


# https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-02-09&endtime=2023-03-09