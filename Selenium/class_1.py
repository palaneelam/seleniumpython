import time

from selenium import webdriver

driver = webdriver.Chrome()
# driver = webdriver.Edge()
# driver = webdriver.Firefox()
time.sleep(5)

driver.get("https://www.ltimindtree.com/")
print("Title of the application is: ", driver.title)

time.sleep(10)
