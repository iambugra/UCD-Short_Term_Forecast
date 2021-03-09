import matplotlib.pyplot as plt
import numpy as np
import os

def get_avlb_stats(path):
    exels = []
    for doc in os.listdir(path):
        if doc.split('.')[-1] != 'csv':
            continue
        
        station = doc[:-9]
        exels.append(station)
    
    underscore = []
    [underscore.append(x) for x in exels if x not in underscore]
    result = []
    for x in underscore:
        s = x.replace('_', ' ')
        s = s.upper()
        result.append(s)
    
    return result


def create_valid_path(path_to_dir, station, year):
    resulting_path = path_to_dir
    resulting_path = resulting_path + '/'
    
    lower_station = station.lower()
    undscd_station = lower_station.replace(' ', '_')

    resulting_path = resulting_path + undscd_station + '_' + str(year) + '.csv'
    return resulting_path


def capitalize_first_letters(station):
    station_names = station.split(' ')
    lower_station = []
    for x in station_names:
        fl_upper = x.lower()
        fl_upper = fl_upper.capitalize()
        lower_station.append(fl_upper)
    result = ' '.join(lower_station)
    return result