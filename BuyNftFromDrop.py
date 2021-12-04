import os
import runpy
import time
import winsound

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pathlib
import random

# For Sound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 2500  # Set Duration To 1000 ms == 1 second

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
buying_limits = 10

# TODO: You need to put your NFT link here
NFT_link = "https://wpt.thetadrop.com/drop/drop_h3kf955wed8em15bv0s24s1d7jk"

# This is for Single Buy Button
buy_xpath = "//button[normalize-space()='Buy Now']"
# buy_xpath = "/html[1]/body[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]"

# Experiment With Others
# buy_xpath = "//button[normalize-space()='Buy']"
# buy_xpath = "(//button[@type='button'][normalize-space()='View Bids'])"
# buy_xpath = "/html[1]/body[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]"

# This is for Multiple Buy Button
# buy_xpath = "(//button[@type='button'][normalize-space()='Buy Now'])"
# NFT_Number = 1

driver = webdriver.Chrome(r"../thetadrop/chromedriver.exe", chrome_options=chrome_options)


# print(input(" Connect your waller address :"))
driver.implicitly_wait(10)
driver.get(NFT_link)


# print(input("Start Project ..... :"))

try:
    for i in range(buying_limits):
        driver.implicitly_wait(1)
        driver.get(NFT_link)
        driver.implicitly_wait(4)

        # This is for Single Buy Button
        try:
            deposit_elements = driver.find_element_by_xpath(buy_xpath)
            print(deposit_elements.text)
            print(len(deposit_elements.text))
            if len(deposit_elements.text) > 2:
                # print(input("Start Project ..... :"))
                deposit_elements.click()
            else:
                print("Check the x path")
                print("Buy Button not found")
                print("Need Administrator to fixed the bugs")
                winsound.Beep(frequency, 5000)
                time.sleep(10)
                # print(input("Start Project ..... :"))
        except:
            print("Buy Button not found")
            print("Need Administrator to fixed the bugs")
            winsound.Beep(frequency, 5000)
            time.sleep(10)
            # print(input("Start Project ..... :"))

# This is for Multiple Buy Button
        # deposit_elements = driver.find_elements_by_xpath(buy_xpath)
        # print(len(deposit_elements))
        # print(deposit_elements)
        # print(input("Start Project ..... :"))
        # deposit_elements[NFT_Number - 1].click()

        try:
            Pay_with_TFuel_elements = driver.find_element_by_xpath("//button[normalize-space()='Pay with TFUEL']")
            Pay_with_TFuel_elements.click()
            print("Buying " + str(i) + " no nft")
        except:
            print("Pay with TFUEL not found")
            print("Need Administrator to fixed the bugs")
            winsound.Beep(frequency, 5000)
            time.sleep(10)
            # print(input("Start Project ..... :"))

except:
    driver.quit()
    time.sleep(2)
    winsound.Beep(frequency, duration)
    print("Need Administrator to fixed the bugs")
    runpy.run_path(path_name='../thetadrop/BuyNftFromDrop.py')




