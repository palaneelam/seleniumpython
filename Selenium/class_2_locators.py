import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

URL = "https://edwheel.com/index.php/selenium-practice/"
def openBrowser(browserName):
    if browserName =='chrome':
        chromeDriver = webdriver.Chrome()
        return chromeDriver
    else:
        print("Wrong Browser")
        return "none"

def openApplication(chromeDriver, url):
    chromeDriver.get(url)
    chromeDriver.maximize_window()

driver = openBrowser('chrome')
openApplication(driver, URL)


# time.sleep(5)
# print("-----------Lets Identify the Label field 'HEADING'----------")
# page_Heading1 = driver.find_element(By.XPATH, "//h1[@class='title-post entry-title']")
# page_Heading2 = driver.find_element(By.XPATH,  "//h1[text()='Selenium Practice']")
# print(f"Label of page_Heading1: is {page_Heading1.text}")
# print(f"Label of page_Heading2: is {page_Heading2.text}")
# print("-----------Lets Identify the Label field 'NAME'----------")
#
# label_Field_by_method_1_name = driver.find_element(By.XPATH , "//label[@for='name']")
# print(f"label_Field_by_method_1_name: ", label_Field_by_method_1_name.text)
# time.sleep(2)
# label_Field_by_method_2_name = driver.find_element(By.XPATH , "//label[text()='Name:']")
# print(f"label_Field_by_method_2_name: ", label_Field_by_method_2_name.text)
# time.sleep(2)
# print("-----------Lets Identify the input field 'name'----------")
# input_text_by_m_1_name = driver.find_element(By.ID, "name")
# input_text_by_m_1_name.send_keys("Manoranjan - ID")
# time.sleep(1)
# input_text_by_m_2_name = driver.find_element(By.NAME, "name")
# input_text_by_m_2_name.send_keys("Manoranjan DUBEY - NAME")
# time.sleep(1)
# input_text_by_m_3_name = driver.find_element(By.XPATH, "//input[@id='name']")
# input_text_by_m_3_name.send_keys("Manoranjan DUBEY - XPATH")
# time.sleep(1)
# input_text_by_m_4_name = driver.find_element(By.XPATH, "//input[@name='name']")
# input_text_by_m_4_name.send_keys("Manoranjan DUBEY - XPATH")
#
# time.sleep(1)
# input_text_by_m_5_name = driver.find_element(By.CSS_SELECTOR, "#name")
# input_text_by_m_5_name.send_keys("Manoranjan DUBEY - CSS_SELECTOR by ID")

# time.sleep(3)
# input_text_by_m_5_name = driver.find_element(By.CSS_SELECTOR, ".name")
# input_text_by_m_5_name.send_keys("Manoranjan DUBEY - CSS_SELECTOR by ID")

print("-----------Lets Identify the input field 'email'----------")


print("-----------Lets Identify the input field 'dropDown'----------")

dropDown = driver.find_element(By.ID, "dropdown")
select_dp_value = Select(dropDown)
select_dp_value.select_by_value("DPValue1")
time.sleep(3)
select_dp_value.select_by_index(1)
time.sleep(3)
select_dp_value.select_by_visible_text("DPValue 3")

print("-----------Lets Identify the input field 'ListBox'----------")
listBox = driver.find_element(By.ID, "listbox")
select_listBox_value = Select(listBox)
select_listBox_value.select_by_value("list1")
time.sleep(3)
select_listBox_value.select_by_index(1)
time.sleep(3)
select_listBox_value.select_by_visible_text("List 4")
time.sleep(5)
select_listBox_value.deselect_by_value("list1")


time.sleep(10)

