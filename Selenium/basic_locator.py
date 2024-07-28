import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)

driver.get("https://edwheel.com/index.php/selenium-practice/")
print("Title of the application is: ", driver.title)
print("URL of the application is: ", driver.current_url)

# by ID
name_input_txt = driver.find_element(By.ID, "name")
name_input_txt.send_keys("Manoranjan")
time.sleep(5)

# by NAME
name_input_txt = driver.find_element(By.NAME, "name")
name_input_txt.send_keys("Manoranjan DUBEY")
time.sleep(5)

# by ClassName
headertext = driver.find_element(By.CLASS_NAME,"title-post").text
print("Header text: ", headertext)
time.sleep(5)

# by Link_Text
link_elemnt_full = driver.find_element(By.LINK_TEXT, "Sample Link")
print("Text of the link is:", link_elemnt_full.text)
link_elemnt_full.click()

# by Partial link text
link_elemnt_partial = driver.find_element(By.PARTIAL_LINK_TEXT, "Sample")
print("Text of the link is:", link_elemnt_partial.text)
link_elemnt_partial.click()

# by CSS SELECTORS -  by ID (# - for ID)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Neelam")
time.sleep(2)

# by CSS SELECTORS -  by NAME (. - for Class)
headertext_class = driver.find_element(By.CSS_SELECTOR, ".title-post").text
print("Header text headertext_class: ", headertext_class)
time.sleep(3)

# by CSS SELECTORS -  by TAG and CLASS ()
headertext_tag_class = driver.find_element(By.CSS_SELECTOR, "h1.entry-title")
headertext_by_tag_class = headertext_tag_class.text
print("header text by headertext_by_tag_class is:", headertext_by_tag_class)

# by CSS SELECTORS -  by NAME TAG and attributes ()
headertext_Tag_n_Attr = driver.find_element(By.CSS_SELECTOR, "h1[class='title-post entry-title']")
headertext_Tag_n_Attr_txt = headertext_Tag_n_Attr.text
print("header text is:", headertext_Tag_n_Attr_txt)

driver.find_element(By.CSS_SELECTOR, "input[id='name']").send_keys("MD")
time.sleep(5)

print("=======================Done====================================")