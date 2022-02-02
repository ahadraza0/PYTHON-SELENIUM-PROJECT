from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r"C:/Users/HCC/Desktop/Pycharm-pro/chromedriver/chromedriver.exe")
driver.get('http://www.way2automation.com/python/training/selenium-python-training.html')
user= driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input')
user.send_keys('programmingofficialsite@gmail.com')
man=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
man.send_keys('ahadraza')
women=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
women.send_keys('03325514947')
gender=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
gender.send_keys('Pakistan')
driver.find_element_by_xpath('//*[@id="i30"]/div[3]/div').click()
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div[1]/div/div/span/span').click()