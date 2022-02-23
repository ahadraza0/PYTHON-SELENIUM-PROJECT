from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/AHAD RAZA/Downloads/chromedriver.exe")

driver.get("https://www.facebook.com/")


email = driver.find_element(By.ID, "email")


email.send_keys("programmingofficialsite@outlook.com")


password = driver.find_element(By.ID, "pass")


password.send_keys("ahadrazaofficial07")


click1 = driver.find_element(By.NAME, "login")

click1.click()

driver.implicitly_wait(10)
driver.close(10)