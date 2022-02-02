from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:/Users/HCC/Desktop/Pycharm-pro/chromedriver/chromedriver_win32/chromedriver.exe")
driver.get('https://www.instagram.com/')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('abdulahadraza02@gmail.com')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('hellodear')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()