from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pynput.keyboard



def add_station(station, driver):
    togle_state = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//div[@class='single']//div[@class='placeholder']")))
    togle_state.click()

    enter_state = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//div[@class='filter']/input[1]")))
    enter_state.clear()
    enter_state.send_keys("Delhi")
    enter_state.send_keys(Keys.RETURN)


    toggle_city = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//div[@class='single']//div[@class='placeholder']")))
    toggle_city.click()

    enter_city = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//div[@class='filter']/input[1]")))
    enter_city.clear()
    enter_city.send_keys("Delhi")
    enter_city.send_keys(Keys.RETURN)


    toggle_station = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//div[@class='single']//div[@class='placeholder']")))
    toggle_station.click()

    enter_station = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//div[@class='filter']/input[1]")))
    enter_station.clear()
    enter_station.send_keys(station)
    enter_station.send_keys(Keys.RETURN)


    togle_polutants = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//div[@class='selected-list']//div[@class='c-btn']")))
    togle_polutants.click()

    togle_PM10 = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//li[@class='pure-checkbox']//label[text()='PM10']")))
    togle_PM10.click()
    togle_PM25 = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//li[@class='pure-checkbox']//label[text()='PM2.5']")))
    togle_PM25.click()
    togle_NH3 = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//li[@class='pure-checkbox']//label[text()='NH3']")))
    togle_NH3.click()
    togle_NO2 = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//li[@class='pure-checkbox']//label[text()='NO2']")))
    togle_NO2.click()
    togle_CO = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//li[@class='pure-checkbox']//label[text()='CO']")))
    togle_CO.click()
    togle_SO2 = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//li[@class='pure-checkbox']//label[text()='SO2']")))
    togle_SO2.click()
    togle_OZONE = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//li[@class='pure-checkbox']//label[text()='Ozone']")))
    togle_OZONE.click()


    button_station = driver.find_element_by_xpath("//div[@class='col-md-12']//button[text()='Add Station']")
    button_station.click()


def period_criteria(driver):
    toggle_criteria = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.col-md-12:nth-child(5) > div:nth-child(2) > div:nth-child(1) > ng-select:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")))
    toggle_criteria.click()

    enter_criteria = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//div[@style='top: 32px; left: 0px; width: 245px;']//div[@class='filter']/input[1]")))
    enter_criteria.clear()
    enter_criteria.send_keys("15 Minute")
    enter_criteria.send_keys(Keys.RETURN)


def begin_date(year, driver, i):

    togle_calender_from = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='fromDate']//div[@class='wc-date-container']")))
    togle_calender_from.click()     

    year_dropdown_from = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='fromDate']//div[@class='year-dropdown']")))
    year_dropdown_from.click()  

    select_year_from = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='fromDate']//span[@id='" + str(year+i) + "']")))
    select_year_from.click()

    month_dropdown_from = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='fromDate']//div[@class='month-year']")))
    month_dropdown_from.click()     

    select_month_from = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='fromDate']//span[@id='JAN']")))
    select_month_from.click()       

    select_day_from = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='fromDate']//table[@class='calendar-days']//span[text()='1']")))
    select_day_from.click()    

    done_from = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='fromDate']//div[@class='cal-util']")))
    done_from.click()       


def end_date(year, driver, i):

    togle_calender_to = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='toDate']//div[@class='wc-date-container']")))
    togle_calender_to.click()       

    year_dropdown_to = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='toDate']//div[@class='year-dropdown']")))
    year_dropdown_to.click()       

    select_year_to = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='toDate']//span[@id='" + str(year+i) + "']")))
    select_year_to.click()

    month_dropdown_to = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='toDate']//div[@class='month-year']")))
    month_dropdown_to.click()       

    select_month_to = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='toDate']//span[@id='DEC']")))
    select_month_to.click()    

    select_day_to = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='toDate']//table[@class='calendar-days']//span[text()='31']")))
    select_day_to.click()

    toggle_clock = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='toDate']//span[@class='fa fa-clock-o']")))
    toggle_clock.click()        

    
    toggle_hour = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='toDate']//div[@class='hour']/input")))
    toggle_hour.click()
    toggle_hour.send_keys(Keys.ARROW_RIGHT)
    pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
    pynput.keyboard.Controller().release(pynput.keyboard.Key.backspace)
    pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
    pynput.keyboard.Controller().release(pynput.keyboard.Key.backspace)
    pynput.keyboard.Controller().press("1")
    pynput.keyboard.Controller().release("1")
    pynput.keyboard.Controller().press("1")
    pynput.keyboard.Controller().release("1")

    sleep(0.5) # this is required

    toggle_minute = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='toDate']//div[@class='minutes']/input")))
    toggle_minute.click()
    toggle_minute.send_keys(Keys.ARROW_RIGHT)
    pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
    pynput.keyboard.Controller().release(pynput.keyboard.Key.backspace)
    pynput.keyboard.Controller().press(pynput.keyboard.Key.backspace)
    pynput.keyboard.Controller().release(pynput.keyboard.Key.backspace)
    pynput.keyboard.Controller().press("4")
    pynput.keyboard.Controller().release("4")
    pynput.keyboard.Controller().press("5")
    pynput.keyboard.Controller().release("5")


    toggle_pm = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='toDate']//button[text()='PM']")))
    toggle_pm.click()

    toggle_set_time = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='toDate']//button[text()='Set Time']")))
    toggle_set_time.click()

    done_to = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//angular2-date-picker[@ng-reflect-name='toDate']//div[@class='cal-util']")))
    done_to.click()


def submit_page(driver):
    submit = driver.find_element_by_xpath("//div[@class='col-md-12']//button[text()='Submit']")
    submit.click()


def get_excel(driver):
    toggle_excel = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, "//a[@data-tooltip='Excel']")))
    toggle_excel.click()


def keybd_press(driver):
    pynput.keyboard.Controller().press(pynput.keyboard.Key.down)
    pynput.keyboard.Controller().release(pynput.keyboard.Key.down)
    sleep(0.5)
    pynput.keyboard.Controller().press(pynput.keyboard.Key.enter)
    pynput.keyboard.Controller().release(pynput.keyboard.Key.enter)