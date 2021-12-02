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

# TODO : fixed url path and test in Trven Device
driver = webdriver.Chrome(r"../thetadrop/chromedriver.exe", chrome_options=chrome_options)


# print(input(" Connect your waller address :"))
driver.implicitly_wait(10)
# TODO : Original NFT Like will be Different Make a Variable for that
driver.get("https://wpt.thetadrop.com/drop/drop_h3kf955wed8em15bv0s24s1d7jk")


print(input("Start Project ..... :"))

deposit_elements = driver.find_element_by_xpath("(//button[.='Deposit funds'])[2]")
deposit_elements.click()

deposit_TFuel_elements = driver.find_element_by_xpath("//button[normalize-space()='Deposit TFuel']")
deposit_TFuel_elements.click()

i_agree_elements = driver.find_element_by_xpath("//button[normalize-space()='I AGREE']")
i_agree_elements.click()

# TODO: Buy NFT and Make Repetitions Using Loop

