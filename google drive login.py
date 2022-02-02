import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:/Users/HCC/Desktop/Pycharm-pro/chromedriver/chromedriver.exe")
driver.get('https://www.google.com/intl/en_zm/drive/')
driver.find_element_by_xpath('//*[@id="drawer"]/div/div[3]/div/a[1]').click()
driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/div').send_keys('programmingofficialsite@gmail.com')
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
