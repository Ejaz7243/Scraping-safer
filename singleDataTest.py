from selenium import driver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time

driver.get('https://safer.fmcsa.dot.gov/CompanySnapshot.aspx')
time.sleep(2)
button = driver.find_element(by="xpath", value="//input[@id='2']")
button.click()

mc = driver.find_element(by="xpath", value="//input[@id='4']")
mc.send_keys("199584")

button2 = driver.find_element(by="xpath", value="//input[@type='SUBMIT']")
button2.click()


time.sleep(1)
checkCarrier = driver.find_element(by="xpath", value="//a[@href='saferhelp.aspx#EntityType']/../..//td")
checkAuth = driver.find_element(by="xpath", value="/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[3]/td[1]")

# print(checkCarrier.text)
# print(checkAuth.text)

if checkCarrier.text == "CARRIER  ":
    if checkAuth.text == "AUTHORIZED FOR Property" or checkAuth.text == "AUTHORIZED FOR Property, HHG" or checkAuth.text == "ACTIVE" or checkAuth.text == "REGISTERED":
        print(checkCarrier.text)
        print(checkAuth.text)

driver.quit()