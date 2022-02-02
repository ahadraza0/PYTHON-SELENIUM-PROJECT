from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r"C:\Users\HCC\Desktop\CHROME DRIVER\chromedriver.exe")
driver.get('https://quran.com/55')
driver.find_element_by_xpath('//*[@id=4902]/div[2]/div[1]/div/a[1]/i').click()