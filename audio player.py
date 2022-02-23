from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/AHAD RAZA/Downloads/chromedriver.exe")

driver.get("https://quran.com/surah-ar-rahman")

driver.maximize_window()

play = driver.find_element(By.ID, "btn-play")

play.click()

driver.implicitly_wait(0)

auto = driver.find_element(By.ID, "btn-scroll")

auto.click()

auto1 = driver.find_element(By.ID, "btn-scroll")

auto1.click()


driver.stop_client()
