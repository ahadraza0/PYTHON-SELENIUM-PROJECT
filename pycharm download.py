from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:/Users/HCC/Desktop/Pycharm-pro/chromedriver/chromedriver.exe")
driver.get('https://www.jetbrains.com/pycharm/')
driver.find_element_by_xpath('/html/body/div[4]').click()