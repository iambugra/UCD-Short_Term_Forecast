import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import stropns
from statsmodels.tsa.stattools import adfuller, kpss
import math
import time
import statsmodels.api as sm 
import warnings
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from statistics import mean
from random import randint
from statsmodels.tsa.holtwinters import ExponentialSmoothing


""" implementation of naive forecasting method """
def naive(size, end_slice, test_size, last_value):
    list_of_lastval = [last_value for x in range(test_size)]
    return list_of_lastval

""" implementation of persistence forecasting method """
def persistence(df, size, st_ind, end_ind, test_size):
    train = []
    test = []
    for i in range(st_ind, end_ind-test_size):
        train.append(df.at[i, 'Pollution data'])
    for i in range(end_ind-test_size, end_ind):
        test.append(df.at[i, 'Pollution data'])

    history = [x for x in train]
    predictions = list()

    for i in range(test_size):
        predictions.append(history[-1])
        history.append(test[i])

    return predictions


""" implementation of simple average forecasting method """
def sim_avg(df, size, st_ind, end_ind, test_size):
    train = []
    for i in range(st_ind, end_ind-test_size):
        train.append(df.at[i, 'Pollution data'])
    means = [round(mean(train),2) for x in range(test_size)]
    return means



start_time = time.time()

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print('Process started at', current_time, '\n')

# absolute path to the csv files
path_to_csvs = '/Users/bugraalparslan/Desktop/short-term-fcast/csv files'

# absolute path to the file which contatins 5 randomly selected samples
# I organized the lines of file as -> station_name month_rank year pollutant
# (I assumed the station_name is consisted of 2 words)
# so this code reads the file according to that.
path_to_clean_data = '/Users/bugraalparslan/Desktop/short-term-fcast/rand_5_data.txt'


with open(path_to_clean_data, 'r') as handle:

    for datum in handle:
        datum = datum.rstrip()
        datum = datum.split(' ')
        
        station = datum[0] + ' ' +  datum[1]
        month_entered = int(datum[2])
        year = int(datum[3])
        pollutant = datum[4]
        period = 'M'
        pollutants = ['PM10', 'PM2.5', 'NH3', 'NO2', 'CO', 'SO2', 'Ozone']

        data = []
     
        with open(stropns.create_valid_path(path_to_csvs, station, year), 'r') as hand:
            for line in hand:
                line = line.rstrip()
                line = line.split(';')
                index = pollutants.index(pollutant)+2
                
                if int(line[0].split('-')[1]) == month_entered:
                    if line[index] == 'None' or line[index] == "" or line[index] == '0':
                        continue

                    val = line[index].replace(",", ".")
                    data.append(float(val))
                
        hand.close()

        d = {'Pollution data':data}
        df = pd.DataFrame(d)

        # number of times this process to be repeated, train size and lead
        no_of_iters = 25
        train_size = 200
        lead = 3

        warnings.filterwarnings('ignore')

        # absolute path to the directory which contains the test results
        # Here I have a directory RES in Desktop and in RES, I grouped the results
        # with respect to their train and lead sizes, e.g., RES/200-3, RES/100-10 etc.
        # In those directories, there are actual test results.
        res_file = open('/Users/bugraalparslan/Desktop/RES/' + str(train_size) + '-' + str(lead) + '/res_' + station[0] + '_' + str(month_entered) + '_' + str(year) + '_' + pollutant + '.csv', 'w')
        res_file.write('Min,Max,Mean,Median,SARIMA,Naive,Persistence,SimpleAverage\n')

        print('{}, {}/{}, {} is being read now.\n'.format(station, month_entered, year, pollutant))

        for i in range(no_of_iters):
            print('#iter={}\ni={}'.format(no_of_iters, i))
            
            try:
                st_index = randint(0, len(data)-train_size-1)
                end_index = st_index + train_size
                print('start ind = {}\nend ind = {}\n'.format(st_index, end_index))

                # forecast
                model=sm.tsa.statespace.SARIMAX(df.iloc[st_index:end_index, 0],order=(2,1,1),seasonal_order=(2,1,1,96), enforce_stationarity=False, enforce_invertibility=False)
                results=model.fit(disp=0)
                df['Forecast'] = round(results.predict(start=train_size-lead,end=train_size-1, dynamic=True),2)

                df['Test data'] = df.iloc[end_index-lead:end_index, 0]

                rmse = math.sqrt(mean_squared_error(df['Test data'].dropna(), df['Forecast'].dropna()))
                naive_list = naive(len(df['Pollution data']), end_index, lead, df.at[end_index-lead-1, 'Pollution data'])
                persistence_list = persistence(df, len(df['Pollution data']), st_index, end_index, lead)
                sim_avg_list = sim_avg(df, len(df['Pollution data']), st_index, end_index, lead)
                
                df = df.replace('NaN',np.NaN)
                
                
                res_file.write('{},'.format(df.iloc[st_index:end_index, 0].min()))
                res_file.write('{},'.format(df.iloc[st_index:end_index, 0].max()))
                res_file.write('{},'.format(round(df.iloc[st_index:end_index, 0].mean(),2)))
                res_file.write('{},'.format(round(df.iloc[st_index:end_index, 0].median(),2)))
                res_file.write('{},'.format(round(rmse,2)))
                res_file.write('{},'.format(round(math.sqrt(mean_squared_error(df['Test data'].dropna(), naive_list)), 2)))
                res_file.write('{},'.format(round(math.sqrt(mean_squared_error(df['Test data'].dropna(), persistence_list)), 2)))
                res_file.write('{}\n'.format(round(math.sqrt(mean_squared_error(df['Test data'].dropna(), sim_avg_list)), 2)))
                
            except:
                res_file.write('Could not forecast\n\n')
                continue

        res_file.close()

        print('\nProcess took {} minutes, {} seconds.\n' .format(round(int((time.time() - start_time)/60), 2), round((time.time() - start_time)%60, 2)))
        start_time = time.time()

handle.close()