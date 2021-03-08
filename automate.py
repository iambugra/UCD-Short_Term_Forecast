from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pynput.keyboard
import defns

print("You will be asked to enter the years of which you need the data. If you need only one year's data, enter that year in both first year and last year.")
sleep(5)

first_year = int(input("Enter the first year: \n"))
last_year = int(input("Enter the last year: \n"))
no_of_years = last_year - first_year + 1

no_of_stations = int(input("Enter the number of stations: \n"))
stations = []
print('Enter the stations: ')
for station in range(no_of_stations):
    station = input()
    stations.append(station)

print('\n\nGetting the data of;')
for i in range(no_of_years):
    print(i+first_year)
sleep(1)
print('For the stations;')
for station in stations:
    print(station)

for j in range(no_of_years):
    for station in stations:
        url = 'https://app.cpcbccr.com/ccr/#/caaqm-dashboard/caaqm-landing/caaqm-comparison-data'
        driver = webdriver.Firefox()
        driver.get(url)

        defns.add_station(station, driver)      # add station

        defns.period_criteria(driver)       # set the criteria to 15-mins      
        defns.begin_date(first_year, driver, j)       # set the begin date     
        defns.end_date(first_year, driver, j)     # set the end date
        defns.submit_page(driver)       # submit the first page
        sleep(300)       # wait till the second page loads
        defns.get_excel(driver)     # download the excel file
        sleep(500)      # wait till excel file is ready
        defns.keybd_press(driver)       # download the excel file
        sleep(200)      # wait to make sure file is downloaded
        driver.quit()       # quit peacefully
