#Implementation of Selenium WebDriver with Python using PyTest
 
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
 
def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome()
    
    chrome_driver.get('http://localhost:8501')
    chrome_driver.maximize_window()
 
    name_text_field = chrome_driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/section/div/div[1]/div[3]/div/div[1]/div/input').send_keys('Sushant')
    pincode_text_field = chrome_driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/section/div/div[1]/div[4]/div/div[1]/div/input').send_keys('110077')
    category_dropdown_field = chrome_driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/section/div/div[1]/div[5]/div/div/div/div[1]').send_keys('110077')
    preference_dropdown1_field = chrome_driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/section/div/div[1]/div[6]/div/div/div/div[1]').send_keys('110077')
    preference_dropdown2_field = chrome_driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/section/div/div[1]/div[7]/div/div/div/div[1]').send_keys('110077')
    preference_dropdown3_field = chrome_driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/section/div/div[1]/div[8]/div/div/div/div[1]').send_keys('110077')
    process_button = chrome_driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/section/div/div[1]/div[9]/div/button').click()
    sleep(5)
    success = chrome_driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/section/div/div[1]/div[10]/div/div')
    if(success == "This is Technical"):
        print("Tests Passed Successfully")
    
    sleep(2)
    chrome_driver.close()