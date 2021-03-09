import matplotlib.pyplot as plt
import numpy as np
import os

# function giving the available stations in the path
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

# function getting absolute path to the directory to the csv files, a station and a year
# and it returns an absolute path in the form 'PATH/TO/DIRECTORY/STATION_NAME_YEAR.csv'
def create_valid_path(path_to_dir, station, year):
    resulting_path = path_to_dir
    resulting_path = resulting_path + '/'
    
    lower_station = station.lower()
    undscd_station = lower_station.replace(' ', '_')

    resulting_path = resulting_path + undscd_station + '_' + str(year) + '.csv'
    return resulting_path

# gets a station and capitalizes the first letters of each word in the station name
def capitalize_first_letters(station):
    station_names = station.split(' ')
    lower_station = []
    for x in station_names:
        fl_upper = x.lower()
        fl_upper = fl_upper.capitalize()
        lower_station.append(fl_upper)
    result = ' '.join(lower_station)
    return result