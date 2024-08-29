'''
Uploads data extracted from Earthquake API onto
file under the name given by the user.
'''

import json


def file_upload(eq_data, file_name):
    '''
    Take the Earthquake API data and writes it
    onto a formal file that can be accessed
    outside of the program under the file name that
    the user provided in the very beginning
    '''
    with open(file_name, 'w', encoding='utf-8') as out_file:
        json.dump(eq_data, out_file)
