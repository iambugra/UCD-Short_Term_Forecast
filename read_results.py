# res_A_11_2018_PM10.csv
# res_P_10_2018_Ozone.csv
# res_P_7_2018_PM25.csv
# res_A_11_2018_PM25.csv
# res_P_2_2018_PM10.csv

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from statistics import mean

# plot histogram of data
def plot_hist(x):
    plt.hist(x, bins=25)
    plt.ylabel('Number of results')
    plt.xlabel('RMSE values')
    plt.show()

# function that gets a list as input and returns the same list whose elements reside
# between the interquartile range and it also returns the number of outliers in the input 
# list
def outliers_removed_list(lst):
    sorted_data = lst
    sorted_data.sort()
    q1, q3 = np.percentile(sorted_data, [25,75])
    iqr = q3-q1
    lower_bound = q1 -(1.5 * iqr) 
    upper_bound = q3 +(1.5 * iqr)
    out_removed = [x for x in sorted_data if x > lower_bound and x < upper_bound] 
    outlier_count = len(lst) - len(out_removed)
    return out_removed, outlier_count


def result_of_all_sarimas():
    all_sarima = []

    for tr in [100, 200]:
        for test in [5, 10 ,15]:
            for st in ['res_A_11_2018_PM10.csv', 'res_P_10_2018_Ozone.csv', 'res_P_7_2018_PM25.csv', 'res_A_11_2018_PM25.csv', 'res_P_2_2018_PM10.csv']:
                df = pd.read_csv('/Users/bugraalparslan/Desktop/results-all-together/{}-{}/{}'.format(tr, test, st))
                for x in df['SARIMA'].values.tolist():
                    all_sarima.append(x)


    within_iqr, count_of_outliers = outliers_removed_list(all_sarima)

    count_corrects = len(all_sarima) - count_of_outliers
    perc_corrects = (750-count_of_outliers)/750*100

    print('Number of results that lie within iqr: {}'.format(count_corrects))
    print('Number of outliers: {}'.format(count_of_outliers))
    print('Percentage of results in iqr: {:.1f}%'.format(perc_corrects))

    below_100 = [x for x in within_iqr if x < 100]

    print('Average of the set of RMSEs whose value is less than 100: {:.1f}'.format(mean(below_100)))
    print('Number of values whose RMSE is less than 100: {}'.format(len(below_100)))
    print('Percentage of those below 100 among all 750: {:.1f}'.format(len(below_100)/len(all_sarima)*100))

    plot_hist(within_iqr)


def comparsion_table(tr, test):
    s = []
    n, p, sav = 0, 0, 0


    # iterate through all the test results
    for st in ['res_A_11_2018_PM10.csv', 'res_P_10_2018_Ozone.csv', 'res_P_7_2018_PM25.csv', 'res_A_11_2018_PM25.csv', 'res_P_2_2018_PM10.csv']:
        df = pd.read_csv('/Users/bugraalparslan/Desktop/results-all-together/{}-{}/{}'.format(tr, test, st))
        
        for x in df['SARIMA'].values.tolist():
            if x < 100:
                s.append(x)
        n = round(df['Naive'].mean(), 2)
        p = round(df['Persistence'].mean(), 2)
        sav = round(df['SimpleAverage'].mean(), 2)

    s, _ = outliers_removed_list(s)

    print('Results for train = {} and test = {}\nSARIMA = {}\nPersistence = {}\nSimpleAverage = {}'.format(tr, test, round(mean(s), 2), p, sav))


result_of_all_sarimas()
print('--------------------------------------------------------------------')

# test and train sizes
train = 100
test = 15
comparsion_table(train, test) 