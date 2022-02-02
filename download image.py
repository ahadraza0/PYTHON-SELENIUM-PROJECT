import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r"C:\Users\HCC\Desktop\CHROME DRIVER\chromedriver.exe")
driver.get("https://www.daraz.pk/")
ahad = driver.find_elements_by_tag_name('img')
print(len (ahad))
count = 0
for i in ahad:
    src = i.get_attribute ('src')
    try:
        urllib.request.urlretrieve (src, "catpure"+str(count)+".png")
        print(str(count)+" Image  downloaded")

    except:
        print("Failed to download Image!")
    count = count + 1
