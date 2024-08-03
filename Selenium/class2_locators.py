# 1. CSS - cascading style sheets
# Basics -
# 1. tag name selectors
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
elements = driver.find_element(By.CSS_SELECTOR, "input")
# elements = driver.find_element_by_css_selector("input")

# 2. ID selector
elements = driver.find_element(By.ID, "#name")

# 3. class selector
elements = driver.find_element(By.CSS_SELECTOR, ".title-post")

# 4. Attribute selector
elements = driver.find_element(By.CSS_SELECTOR, "input[id = 'name']")

# Advance CSS Selectors
# 1. Descendant Selector
elements = driver.find_element(By.CSS_SELECTOR, "form input")

# 2. Child Selector
elements = driver.find_element(By.CSS_SELECTOR, "form > input")

# 3. Adjacent Sibling Selector
elements = driver.find_element(By.CSS_SELECTOR, "input + label")

# 4. General Sibling Selector
elements = driver.find_element(By.CSS_SELECTOR, "input ~ label")

# 5. Pusedo classes
elements = driver.find_element(By.CSS_SELECTOR, "ul li:first-child")

# 6. substring matching - start with the value
elements = driver.find_element(By.CSS_SELECTOR, "input[id^='user']")

# 7. substring matching - end with the value
elements = driver.find_element(By.CSS_SELECTOR, "input[id$='name']")

# 8. substring matching - contains any the value. For eg. - C25ordercreated23456
elements = driver.find_element(By.CSS_SELECTOR, "input[id*='user']")

# **************************************************************************

# XPATH - XML Path
# Absolute XPATH
driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/main/article/div/div/div/div[1]/div/div/div/input[1]')

# Relative XPATH
driver.find_element(By.XPATH, "//input[@id='name']")

driver.find_element(By.XPATH, "//input[@type='text' and @id='name]")

# using attributes
driver.find_element(By.XPATH, '//input[@id="name"]')
driver.find_element(By.XPATH, '//input[@name="name"]')
driver.find_element(By.XPATH, '//input[@class="title-post"]')

# using text()
driver.find_element(By.XPATH, "//button[text()='Reset Dummy Button']")

# using contains()
driver.find_element(By.XPATH, "//button[contains(text(),'Reset Dummy Button')]")
driver.find_element(By.XPATH, "//input[contains(@name,'name')]")

# starts-with
driver.find_element(By.XPATH, "//input[starts-with(@name,'na')]")

# parent-child relationship
driver.find_element(By.XPATH, "//div/child::input[1]")





































