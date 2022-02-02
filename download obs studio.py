from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver =webdriver.Chrome(executable_path=r"C:\Users\HCC\Desktop\CHROME DRIVER\chromedriver.exe")
driver.get('https://obsproject.com/download')
driver.find_element_by_xpath('//*[@id="win_blurb"]/div[2]/a[4]').click()