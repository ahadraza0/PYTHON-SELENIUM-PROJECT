from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r"C:/Users/HCC/Desktop/Pycharm-pro/chromedriver/chromedriver.exe")
driver.get('https://www.mozilla.org/en-US/firefox/new/')
driver.find_element_by_xpath('//*[@id="download-button-thanks"]/a').click()