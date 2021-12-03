import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import random

# Setting the chrome_options
global chrome_options
chrome_options = Options()
scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument('--profile-directory=Profile 8')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")

# TODO: How much you want to buy
buying_limits = 20

# TODO: You need to put your NFT link here
NFT_link = "https://thetatv.thetadrop.com/order/saleord_3vpe9m5s7mhty4yn3xssdbun"

buy_xpath = "//button[normalize-space()='Buy']"


# TODO : fixed url path and test in Trven Device
driver = webdriver.Chrome(r"../thetadrop/chromedriver.exe", chrome_options=chrome_options)


# print(input(" Connect your waller address :"))
driver.implicitly_wait(10)
driver.get(NFT_link)


print(input("Start Project ..... :"))

for i in range(buying_limits):
    driver.implicitly_wait(1)
    driver.get(NFT_link)
    deposit_elements = driver.find_element_by_xpath(buy_xpath)
    deposit_elements.click()

    Pay_with_TFuel_elements = driver.find_element_by_xpath("//button[normalize-space()='Pay with TFUEL']")
    Pay_with_TFuel_elements.click()
    print("Buying " + str(i) + " no nft")




