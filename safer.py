from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
# import time


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

mcNumber = []
phoneNumber = []
carrier = []
powerUnit = []
unitDriver = []
authority = []
i = 1457315

while i <= 1470000:
    driver.get('https://safer.fmcsa.dot.gov/CompanySnapshot.aspx')

    # for USDOT number find
    # button = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@id='1']"))) 
    button = WebDriverWait(driver, 0.2).until(ec.presence_of_element_located((By.XPATH, "//input[@id='2']")))  # for wait
    # button = driver.find_element(by="xpath", value="//input[@id='2']") # without wait
    button.click()

    mc = driver.find_element(by="xpath", value="//input[@id='4']")
    mc.send_keys(i)

    button2 = driver.find_element(by="xpath", value="//input[@type='SUBMIT']")
    button2.click()

    try:
        # time.sleep(1)
        checkCarrier = WebDriverWait(driver, 0.25).until(ec.presence_of_element_located((By.XPATH, "//a[@href='saferhelp.aspx#EntityType']/../..//td"))).text  # for wait
        # checkCarrier = driver.find_element(by="xpath", value="//a[@href='saferhelp.aspx#EntityType']/../..//td")
        checkAuth = driver.find_element(by="xpath",
                                        value="/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[3]/td[1]").text
        if checkCarrier == "CARRIER  ":
            if checkAuth == "AUTHORIZED FOR Property" or checkAuth == "AUTHORIZED FOR Property, HHG" or checkAuth == "ACTIVE" or checkAuth == "REGISTERED":
                carrier.append(checkCarrier)
                authority.append(checkAuth)
                phoneNumber.append(driver.find_element(by="xpath",
                                                       value="/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[7]/td").text)
                try:
                    mc = driver.find_element(by="xpath",
                                             value="/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[10]/td[1]/a").text
                except:
                    mc = "None"
                mcNumber.append(mc)
                powerUnit.append(driver.find_element(by="xpath",
                                                     value="/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[11]/td[1]").text)
                unitDriver.append(driver.find_element(by="xpath",
                                                      value="/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[11]/td[2]").text)
                print(mc + "\n")
    except:
        pass

    df_lead = pd.DataFrame(
        {"Entity Type": carrier, "Operating Status": authority, 'MC Number': mcNumber, 'Phone Number': phoneNumber,
         'PowerUnit': powerUnit, 'Driver': unitDriver})
    df_lead.to_csv('Leads3.csv', index=False)

    i = i+1

driver.quit()



# -------------------------single checking for testing purpose -----------------------------------

# driver.get('https://safer.fmcsa.dot.gov/CompanySnapshot.aspx')
# time.sleep(2)
# button = driver.find_element(by="xpath", value="//input[@id='2']")
# button.click()
#
# mc = driver.find_element(by="xpath", value="//input[@id='4']")
# mc.send_keys("199584")
#
# button2 = driver.find_element(by="xpath", value="//input[@type='SUBMIT']")
# button2.click()
#
#
# time.sleep(1)
# checkCarrier = driver.find_element(by="xpath", value="//a[@href='saferhelp.aspx#EntityType']/../..//td")
# checkAuth = driver.find_element(by="xpath", value="/html/body/p/table/tbody/tr[2]/td/table/tbody/tr[2]/td/center[1]/table/tbody/tr[3]/td[1]")
#
# # print(checkCarrier.text)
# # print(checkAuth.text)
#
# if checkCarrier.text == "CARRIER  ":
#     if checkAuth.text == "AUTHORIZED FOR Property" or checkAuth.text == "AUTHORIZED FOR Property, HHG" or checkAuth.text == "ACTIVE" or checkAuth.text == "REGISTERED":
#         print(checkCarrier.text)
#         print(checkAuth.text)
#
# driver.quit()
