import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.service import Service
#
# service_obj = Service("C:\chromdriver.exe")

driver = webdriver.Chrome()

# driver = webdriver.Edge()
# driver = webdriver.Firefox()
# webdriver.Safari()

driver.get("https://edwheel.com/index.php/selenium-practice/")
driver.maximize_window()
print("Title of app:",driver.title)
print("Current url",driver.current_url)
# driver.minimize_window()
# driver.get("https://edwheel.com")
# driver.back()
# driver.refresh()
# driver.forward()
# driver.close()

# Locators / object identification
# ID
# driver.find_element(By.ID, "name").send_keys("Neelam")
# time.sleep(5)
#
# driver.find_element(By.ID, "name").clear()
#
# # Name
# driver.find_element(By.NAME, "name").send_keys("Ritu")
# time.sleep(5)
#
# # classname
# headertext = driver.find_element(By.CLASS_NAME, "title-post").text
# print("header text is:", headertext)
#
# # linktext
# # link_elemnt = driver.find_element(By.LINK_TEXT, "Sample Link")
# # print("Text of the link is:", link_elemnt.text)
# # link_elemnt.click()
#
# # partial link text
# link_elemnt = driver.find_element(By.PARTIAL_LINK_TEXT, "Sample")
# print("Text of the link is:", link_elemnt.text)
# link_elemnt.click()

# css selector
# 1. css seelctor by ID
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Sujeet")
time.sleep(5)

# 2. css selector by class
# headertext = driver.find_element(By.CSS_SELECTOR, ".title-post").text
# print("header text is:", headertext)

# 3. a. css selector by using tag and class
headertext = driver.find_element(By.CSS_SELECTOR, "h1.entry-title").text
print("header text is:", headertext)

# 3. b. css selector by using tag and attribute
headertext = driver.find_element(By.CSS_SELECTOR, "h1[class='entry-title']").text
print("header text is:", headertext)
driver.find_element(By.CSS_SELECTOR, "input[id='name']").send_keys("MD")
time.sleep(5)



















