from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\HCC\Desktop\CHROME DRIVER\chromedriver.exe')
driver.get('https://gameloop.fun/')
driver.find_element_by_xpath('//*[@id="select"]/div/ul/li[4]/a').click()
driver.find_element_by_xpath('//*[@id="top"]/div[2]/div/a').click()
#driver.find_element_by_xpath('username').send_keys('billas')
#driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
