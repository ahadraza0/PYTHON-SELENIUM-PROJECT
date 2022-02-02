from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver =webdriver.Chrome(executable_path="C:/Users/HCC/Desktop/Pycharm-pro/chromedriver/chromedriver.exe")
driver.get("https://www.messenger.com/")
driver.find_element_by_id("email").send_keys('03365645407')
driver.find_element_by_id("pass").send_keys('BILLAS')
driver.find_element_by_id("loginbutton").click()