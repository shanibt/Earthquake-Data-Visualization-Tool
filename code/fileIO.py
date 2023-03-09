# NAME: Shani Trieu
# EMAIL: shanibt@uci.edu
# STUDENT ID: 16539648

import json

def file_upload(EQ_data, file_name):
    out_file = open(file_name, 'w')
    json.dump(EQ_data, out_file)
    out_file.close