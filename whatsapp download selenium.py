from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/AHAD RAZA/Downloads/chromedriver.exe")
driver.get('https://www.whatsapp.com/')
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//*[@id="u_0_0_/h"]/div/svg[2]/polygon').click()
driver.find_element(By.XPATH, "//*[@id=u_0_1_LM]/div[1]/ul/li[45]/a/h4").click()
