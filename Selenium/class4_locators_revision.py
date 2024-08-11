import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://edwheel.com/index.php/selenium-practice/")
driver.maximize_window()

# driver.find_element(By.ID, "name").send_keys("Neelam Pal")
# driver.find_element(By.NAME, "email").send_keys("neelam@testautomationcoach.com")
#
# # txt_label_heading = driver.find_element(By.CLASS_NAME, "title-post").text
# # print("heading is:", txt_label_heading)
# #
# #
# # # driver.find_element(By.LINK_TEXT, "Sample Link").click()
# # # driver.find_element(By.PARTIAL_LINK_TEXT, "Link").click()
# #
# # txt_label_heading = driver.find_element(By.TAG_NAME, "h1").text
# # print("From tagname heading is:", txt_label_heading)
#
# # CSS Selector by ID
# driver.find_element(By.CSS_SELECTOR, "#name").clear()
# driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Ritu")
#
# # CSS Selector by class-name
# # txt_label_heading = driver.find_element(By.CSS_SELECTOR, ".title-post").text
# # print("heading is:", txt_label_heading)
#
# # CSS Selector to locate with tag and class
# txt_label_heading = driver.find_element(By.CSS_SELECTOR, "h1.title-post").text
# print("heading is:", txt_label_heading)
#
# # CSS Selector to locate by tag[attribute=value]
# driver.find_element(By.CSS_SELECTOR, "#name").clear()
# driver.find_element(By.CSS_SELECTOR, "input[id='name']").send_keys("Rudra")
# # driver.find_element(By.CSS_SELECTOR, "h1[class='title-post entry']").send_keys("Rudra")
# driver.find_element(By.CSS_SELECTOR, "select option:first-child")

# Absolute XPATH - starts from root node which html and has single backslash
# drawback - it is brittle in nature
# / : selects from root node
# driver.find_element(By.XPATH, "/html/body/div[6]//div/div/div/main/article/div/div/div/div[1]/div/div/div/input[1]").send_keys("MD")


# Relative xpath
# // : select node from anywhere in html
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("support@edwheel.com")
driver.find_element(By.XPATH, "(//input)[5]").send_keys("MD")

# //input[@type='text' and @id="name"]
# //label[text()='Dropdown Example:']
# //label[contains(text(),'Dropdown')]
# //label[starts-with(text(),'Dropdown')]
# //input[starts-with(@id, 'email')]
# //a[text()='Sample Link']/parent::label
# //select[@id="listbox"]/child::option[1]
# //select[@id="listbox"]/following-sibling::label[2]
# //select[@id="listbox"]/following::label[2]
# //select[@id="listbox"]/preceding-sibling::label[8]
# //select[@id="listbox"]/preceding::label[8]
time.sleep(10)

















