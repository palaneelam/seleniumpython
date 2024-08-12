import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(4)

url = "https://edwheel.com/index.php/selenium-practice/"
driver.get(url)
time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='Accept All']").click()
print("Title: ", driver.title)
print("Curr URL: ", driver.current_url)
# ****************************************************************************
# BY >> ID
# BY >> NAME
# BY >> TAG_NAME
# BY >> CLASS_NAME
# BY >> LINK_TEXT
# BY >> PARTIAL_LINK_TEXT
# BY >> CSS_SELECTOR
# BY >> XPATH

# driver.find_element(By.XPATH)
# driver.find_element(By.XPATH)

# # driver.find_element(By.ID
# driver.find_element(By.ID, "name").send_keys("Manoranjan")
# print("By.ID")

# # driver.find_element(By.NAME
# driver.find_element(By.NAME, "name").send_keys("Manoranjan DUBEY")
# print("By.NAME")

# # driver.find_element(By.TAG_NAME
# print("By.TAG_NAME: ", driver.find_element(By.TAG_NAME, "h1").text)

# # driver.find_element(By.CLASS_NAME
# print("By.CLASS_NAME (Full NAME): ", driver.find_element(By.CLASS_NAME, "title-postentry-title").text)
## - TBD with Neelam
# CLASS_NAME = driver.find_element(By.CLASS_NAME, ".title-post entry-title")
# CLASS_NAME = driver.find_element(By.CLASS_NAME, ".title-post.entry-title")
# print("CLASS_NAME: ", CLASS_NAME.text)
# print("By.CLASS_NAME (Partial NAME-FIRST): ", driver.find_element(By.CLASS_NAME, "title-post").text)
# print("By.CLASS_NAME (Partial NAME-LAST): ", driver.find_element(By.CLASS_NAME, "entry-title").text)

# # driver.find_element(By.LINK_TEXT
# driver.find_element(By.LINK_TEXT, "Sample Link")
# print("By.LINK_TEXT")

# # driver.find_element(By.PARTIAL_LINK_TEXT
# print("By.PARTIAL_LINK_TEXT")
# driver.find_element(By.PARTIAL_LINK_TEXT, "Sample").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Link").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "ple Li").click()
# time.sleep(5)

# # By CSS SELECTOR >> ID -------
# print("By.CSS_SELECTOR, BY Their ID >> #name:")
# driver.find_element(By.CSS_SELECTOR, "#name").send_keys("name - CSS_SELECTOR BY ID")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys(" email - CSS_SELECTOR BY ID")
# driver.find_element(By.CSS_SELECTOR, "#countrySuggestion").send_keys("India")
# time.sleep(5)

# # By CSS SELECTOR >> CLASS NAME -------
# print("By.CSS_SELECTOR, BY Class-Name >> .checkbox-label:")
# print("checkbox-label: ", driver.find_element(By.CSS_SELECTOR, ".checkbox-label").text)
# print("radio-label: ", driver.find_element(By.CSS_SELECTOR, ".radio-label").text)
# time.sleep(5)

# # By CSS SELECTOR >> TAG and CLASS -------
# print("By.CSS_SELECTOR, BY TAG and CLASS")
# Label_Tag_n_Class = driver.find_element(By.CSS_SELECTOR, "h1.title-post")
# print("By.CSS_SELECTOR, BY TAG and CLASS: ", Label_Tag_n_Class)
# time.sleep(5)

# # By CSS SELECTOR >> Attribute selector -------
# # CSS Selector to locate by tag[attribute=value]
# print("By.CSS_SELECTOR, BY Attribute selector")
# time.sleep(5)
# print("By.CSS_SELECTOR, TAG and VALUE", driver.find_element(By.CSS_SELECTOR, "h1[class='title-post entry-title']"))
# print("By.CSS_SELECTOR, TAG and VALUE", driver.find_element(By.CSS_SELECTOR, "h1[class='title-post entry']"))

# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, "input[id = 'name']").send_keys("CSS_SELECTOR - input[id = 'name']")
# driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("CSS_SELECTOR - input[name = 'name']")
# time.sleep(5)

# ****************************************************************
# ADVANCE CSS SELECTOR >>  Descendant Selector
# driver.find_element(By.CSS_SELECTOR, "form input").send_keys("ADVANCE CSS SELECTOR >>  Descendant Selector")

# ADVANCE CSS SELECTOR >>  Child Selector
# driver.find_element(By.CSS_SELECTOR, "form > input").send_keys("ADVANCE CSS SELECTOR >>  Descendant Selector")

# ADVANCE CSS SELECTOR >>  Pusedo classes
# driver.find_element(By.CSS_SELECTOR, "")


# # Advance CSS Selectors
# # 1. Descendant Selector
# elements = driver.find_element(By.CSS_SELECTOR, "form input")
#
# # 2. Child Selector
# elements = driver.find_element(By.CSS_SELECTOR, "form > input")
#
# # 3. Adjacent Sibling Selector
# elements = driver.find_element(By.CSS_SELECTOR, "input + label")
#
# # 4. General Sibling Selector
# elements = driver.find_element(By.CSS_SELECTOR, "input ~ label")
#
# # 5. Pusedo classes
# elements = driver.find_element(By.CSS_SELECTOR, "ul li:first-child")
#
# # 6. substring matching - start with the value
# elements = driver.find_element(By.CSS_SELECTOR, "input[id^='user']")
#
# # 7. substring matching - end with the value
# elements = driver.find_element(By.CSS_SELECTOR, "input[id$='name']")
#
# # 8. substring matching - contains any the value. For eg. - C25ordercreated23456
# elements = driver.find_element(By.CSS_SELECTOR, "input[id*='user']")

# ****************************************************************
# XPATH >>
#     Absolute XPATH - starts from root node which html and has single backslash
#     drawback - it is brittle in nature
#     / : selects from root node
#     driver.find_element(By.XPATH, "/html/body/div[6]//div/div/div/main/article/div/div/div/div[1]/div/div/div/input[1]").send_keys("MD")


# Relative xpath
# // : select node from anywhere in html

# driver.find_element(By.XPATH, "//input[@id='name']").send_keys("By.XPATH, //input[@id='name']")
# time.sleep(3)
# driver.find_element(By.XPATH, "//input[@name='name']").send_keys("By.XPATH, //input[@name='name']")
#
# driver.find_element(By.XPATH, "(//input)[5]").send_keys("INPUT - NAME : By.XPATH, //input)[5]")
# driver.find_element(By.XPATH, "(//input)[6]").send_keys("INPUT - EMAIL : By.XPATH, //input)[6]")
#
# # Combination
# driver.find_element(By.XPATH, "//input[@type='text' and @id='name']").send_keys("INPUT - NAME : By.XPATH >> Combination")
# driver.find_element(By.XPATH, "//input[@type='text' and @name='email']").send_keys("INPUT - EMAIL : By.XPATH >> Combination")
#
label_1 = driver.find_element(By.XPATH, "//label[text()='Name:']").text
print("By.XPATH - Tag and text - Label_1: ", label_1)

label_2_DD = driver.find_element(By.XPATH, "//label[text()='Dropdown Example:']").text
print("By.XPATH - Tag and text - label_2_DD: ", label_2_DD)

print("By.XPATH - Contains: ", driver.find_element(By.XPATH, "//label[contains(text(), 'Checkbox example:')]"))

print("By.XPATH - Contains: ", driver.find_element(By.XPATH, "//label[contains(text(),'Reset Dummy Button:')]"))
print("By.XPATH - Contains: ", driver.find_element(By.XPATH, "//label[contains(text(),'Dummy')]"))
print("By.XPATH - Contains: ", driver.find_element(By.XPATH, "//label[contains(text(),'Button')]"))
print("By.XPATH - Contains: ", driver.find_element(By.XPATH, "//label[contains(text(),'Button')]"))

driver.find_element(By.XPATH, "//label[starts-with(text(),'Radio')][1]")
driver.find_element(By.XPATH, "//label[starts-with(text(),'Switch')][2]")

print("Label:", driver.find_element(By.XPATH, "//input[starts-with(@id,'chbValue1')]").text)
print("Label:", driver.find_element(By.XPATH, "//input[starts-with(@id,'chbValue1')]").text)

print("Print Label: ", driver.find_element(By.XPATH, "//a[text()='Sample Link']/parent::label"))

driver.find_element(By.XPATH, "//select[@id='listbox']/child::option[2]")
driver.find_element(By.XPATH, "//label[@for='sampleLink']/a[1]").click()

print("=============Done===============")

