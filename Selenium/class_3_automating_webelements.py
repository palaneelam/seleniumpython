import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def launch_Browser(browserName):
    if browserName == 'chrome':
        driver = webdriver.Chrome()
    elif browserName == 'firefox':
        driver = webdriver.Firefox()
    else:
        print("Wrong Browser")
        print("NONE")

    return driver


def open_Application(driver, url):
    driver.maximize_window()
    driver.get(url)


url = "https://edwheel.com/index.php/selenium-practice/"
chdriver = launch_Browser("chrome")
open_Application(chdriver, url)


print("Current Page Title: ",chdriver.title)
print("Current Page URL: ",chdriver.current_url)
time.sleep(1)
# ****************************************************************
# time.sleep(5)
# print("-----------Lets Identify the Label field 'HEADING'--------------------------------------")
# page_Heading1 = chdriver.find_element(By.XPATH, "//h1[@class='title-post entry-title']")
# page_Heading2 = chdriver.find_element(By.XPATH,  "//h1[text()='Selenium Practice']")
# print(f"Label of page_Heading1: is {page_Heading1.text}")
# print(f"Label of page_Heading2: is {page_Heading2.text}")
# print("-----------Lets Identify the Label field 'NAME'----------------------------------")
#
# label_Field_by_method_1_name = chdriver.find_element(By.XPATH , "//label[@for='name']")
# print(f"label_Field_by_method_1_name: ", label_Field_by_method_1_name.text)
# time.sleep(2)
# label_Field_by_method_2_name = chdriver.find_element(By.XPATH , "//label[text()='Name:']")
# print(f"label_Field_by_method_2_name: ", label_Field_by_method_2_name.text)
# time.sleep(2)
# print("-----------Lets Identify the input field 'name'---------------------------------------")
# input_text_by_m_1_name = chdriver.find_element(By.ID, "name")
# input_text_by_m_1_name.send_keys("Manoranjan - ID")
# time.sleep(1)
# input_text_by_m_2_name = chdriver.find_element(By.NAME, "name")
# input_text_by_m_2_name.send_keys("Manoranjan DUBEY - NAME")
# time.sleep(1)
# input_text_by_m_3_name = chdriver.find_element(By.XPATH, "//input[@id='name']")
# input_text_by_m_3_name.send_keys("Manoranjan DUBEY - XPATH")
# time.sleep(1)
# input_text_by_m_4_name = chdriver.find_element(By.XPATH, "//input[@name='name']")
# input_text_by_m_4_name.send_keys("Manoranjan DUBEY - XPATH")
#
# time.sleep(1)
# input_text_by_m_5_name = chdriver.find_element(By.CSS_SELECTOR, "#name")
# input_text_by_m_5_name.send_keys("Manoranjan DUBEY - CSS_SELECTOR by ID")
#
# time.sleep(3)
# input_text_by_m_5_name = chdriver.find_element(By.CSS_SELECTOR, ".name")
# input_text_by_m_5_name.send_keys("Manoranjan DUBEY - CSS_SELECTOR by ID")

# print("-----------Lets Identify the input field 'email'---------------------------------")


# print("-----------Lets Identify the input field 'dropDown'------------------------------")
# dropDown = chdriver.find_element(By.ID, "dropdown")
# select_dp_value = Select(dropDown)
# select_dp_value.select_by_value("DPValue1")
# time.sleep(3)
# select_dp_value.select_by_index(1)
# time.sleep(3)
# select_dp_value.select_by_visible_text("DPValue 3")

# print("-----------Lets Identify the input field 'CheckBOX'-------------------------------------------")
#
# check_Box_Label = chdriver.find_element(By.CLASS_NAME, "checkbox-label")
# check_Box_Label
# print("check_Box_Label: ",check_Box_Label.text)
#
# check_Box_1 = chdriver.find_element(By.ID, "chbValue1")
# check_Box_2 = chdriver.find_element(By.ID, "chbValue2")
# check_Box_3 = chdriver.find_element(By.ID, "chbValue3")
#
# print("check_Box_1 is_selected: ", check_Box_1.is_selected())
# print("check_Box_1 is_enabled: ", check_Box_1.is_enabled())
# print("check_Box_1 is_displayed: ", check_Box_1.is_displayed())
# print("check_Box_2 is_selected: ", check_Box_2.is_selected())
# print("check_Box_2 is_enabled: ", check_Box_2.is_enabled())
# print("check_Box_2 is_displayed: ", check_Box_2.is_displayed())
# print("check_Box_3 is_selected: ", check_Box_3.is_selected())
# print("check_Box_3 is_enabled: ", check_Box_3.is_enabled())
# print("check_Box_3 is_displayed: ", check_Box_3.is_displayed())
#
# check_Box_1.click()
# check_Box_3.click()
# print("check_Box_1 is_selected: ", check_Box_1.is_selected())
# print("check_Box_1 is_enabled: ", check_Box_1.is_enabled())
# print("check_Box_1 is_displayed: ", check_Box_1.is_displayed())
# print("check_Box_2 is_selected: ", check_Box_2.is_selected())
# print("check_Box_2 is_enabled: ", check_Box_2.is_enabled())
# print("check_Box_2 is_displayed: ", check_Box_2.is_displayed())
# print("check_Box_3 is_selected: ", check_Box_3.is_selected())
# print("check_Box_3 is_enabled: ", check_Box_3.is_enabled())
# print("check_Box_3 is_displayed: ", check_Box_3.is_displayed())
# check_Box_1.click()
# check_Box_2.click()
# check_Box_3.click()
# print("check_Box_1 is_selected: ", check_Box_1.is_selected())
# print("check_Box_1 is_enabled: ", check_Box_1.is_enabled())
# print("check_Box_1 is_displayed: ", check_Box_1.is_displayed())
# print("check_Box_2 is_selected: ", check_Box_2.is_selected())
# print("check_Box_2 is_enabled: ", check_Box_2.is_enabled())
# print("check_Box_2 is_displayed: ", check_Box_2.is_displayed())
# print("check_Box_3 is_selected: ", check_Box_3.is_selected())
# print("check_Box_3 is_enabled: ", check_Box_3.is_enabled())
# print("check_Box_3 is_displayed: ", check_Box_3.is_displayed())

# print("-----------Lets Identify the input field 'Reset Dummy Button:'-------------------------------------------")
# resetButton = chdriver.find_element(By.ID, "resetButton")
# resetButton.click()
# resetButton_XPATH = chdriver.find_element(By.XPATH, "//button[@id='resetButton']")
# resetButton_XPATH.click()


# print("-----------Lets Identify the input field 'ListBox'----------------------------------------")
# listBox = chdriver.find_element(By.ID, "listbox")
# select_listBox_value = Select(listBox)
# select_listBox_value.select_by_value("list1")
# time.sleep(3)
# select_listBox_value.select_by_index(1)
# time.sleep(3)
# select_listBox_value.select_by_visible_text("List 4")
# time.sleep(5)
# select_listBox_value.deselect_by_value("list1")

# print("-----------Lets Identify the input field 'RADIO'----------------------------------------")
# radio_Btn_Label = chdriver.find_element(By.CLASS_NAME, "radio-label")
# print("radio_Btn_Label: ", radio_Btn_Label.text)
# radio_Btn_1 = chdriver.find_element(By.ID, "radio1")
# radio_Btn_2 = chdriver.find_element(By.XPATH, "//input[@id='radio2']")
# radio_Btn_3 = chdriver.find_element(By.ID, "radio3")
# print("radio_Btn_1 is_selected: ", radio_Btn_1.is_selected())
# print("radio_Btn_1 is_enabled: ", radio_Btn_1.is_enabled())
# print("radio_Btn_1 is_displayed: ", radio_Btn_1.is_displayed())
# print("radio_Btn_2 is_selected: ", radio_Btn_2.is_selected())
# print("radio_Btn_2 is_enabled: ", radio_Btn_2.is_enabled())
# print("radio_Btn_2 is_displayed: ", radio_Btn_2.is_displayed())
# print("radio_Btn_3 is_selected: ", radio_Btn_3.is_selected())
# print("radio_Btn_3 is_enabled: ", radio_Btn_3.is_enabled())
# print("radio_Btn_3 is_displayed: ", radio_Btn_3.is_displayed())
# print()
# radio_Btn_1.click()
# print("radio_Btn_1 clicked")
# print("radio_Btn_1 is_selected: ", radio_Btn_1.is_selected())
# print("radio_Btn_1 is_enabled: ", radio_Btn_1.is_enabled())
# print("radio_Btn_1 is_displayed: ", radio_Btn_1.is_displayed())
# print("radio_Btn_2 is_selected: ", radio_Btn_2.is_selected())
# print("radio_Btn_2 is_enabled: ", radio_Btn_2.is_enabled())
# print("radio_Btn_2 is_displayed: ", radio_Btn_2.is_displayed())
# print("radio_Btn_3 is_selected: ", radio_Btn_3.is_selected())
# print("radio_Btn_3 is_enabled: ", radio_Btn_3.is_enabled())
# print("radio_Btn_3 is_displayed: ", radio_Btn_3.is_displayed())
#
# radio_Btn_2.click()
# print("radio_Btn_2 clicked")
# print("radio_Btn_1 is_selected: ", radio_Btn_1.is_selected())
# print("radio_Btn_1 is_enabled: ", radio_Btn_1.is_enabled())
# print("radio_Btn_1 is_displayed: ", radio_Btn_1.is_displayed())
# print("radio_Btn_2 is_selected: ", radio_Btn_2.is_selected())
# print("radio_Btn_2 is_enabled: ", radio_Btn_2.is_enabled())
# print("radio_Btn_2 is_displayed: ", radio_Btn_2.is_displayed())
# print("radio_Btn_3 is_selected: ", radio_Btn_3.is_selected())
# print("radio_Btn_3 is_enabled: ", radio_Btn_3.is_enabled())
# print("radio_Btn_3 is_displayed: ", radio_Btn_3.is_displayed())
#
# radio_Btn_3.click()
# print("radio_Btn_3 clicked")
# print("radio_Btn_1 is_selected: ", radio_Btn_1.is_selected())
# print("radio_Btn_1 is_enabled: ", radio_Btn_1.is_enabled())
# print("radio_Btn_1 is_displayed: ", radio_Btn_1.is_displayed())
# print("radio_Btn_2 is_selected: ", radio_Btn_2.is_selected())
# print("radio_Btn_2 is_enabled: ", radio_Btn_2.is_enabled())
# print("radio_Btn_2 is_displayed: ", radio_Btn_2.is_displayed())
# print("radio_Btn_3 is_selected: ", radio_Btn_3.is_selected())
# print("radio_Btn_3 is_enabled: ", radio_Btn_3.is_enabled())
# print("radio_Btn_3 is_displayed: ", radio_Btn_3.is_displayed())

# print("-----------Lets Identify the input field 'LINK'------------------------------------------")
# Sample_link_Text = chdriver.find_element(By.LINK_TEXT, "Sample Link")
# Sample_link_Text.click()
#
# Sample_link_PText = chdriver.find_element(By.PARTIAL_LINK_TEXT, "ple L")
# Sample_link_PText.click()


# print("-----------Lets Identify the input field 'Autosuggestion'------------------------------------------")
# # Autosuggestion
# country_Suggestion = chdriver.find_element(By.ID, "countrySuggestion")
# country_Suggestion.send_keys("India")
# # print(country_Suggestion.text)
# print("country_Suggestion: ", country_Suggestion.get_attribute("value"))

# print("-----------Lets Identify the input field 'Switch Window Example:'------------------------------------------")
# switchWindowButton = chdriver.find_element(By.ID, "switchWindowButton")
# switchWindowButton.click()
# chdriver.switch_to
# print("New Tab URL: ", chdriver.current_url)

# print("-----------Lets Identify the input field 'Switch Window Example:'------------------------------------------")
# for i in range(5):
#     print(i)
#     thead = chdriver.find_element(By.XPATH, "//table[@id='sampleTable']/thead/tr/th[1]")
#     thead = chdriver.find_element(By.XPATH, "//table[@id='sampleTable']/thead/tr/th[2]")
#     thead = chdriver.find_element(By.XPATH, "//table[@id='sampleTable']/thead/tr/th[3]")
#     print("thead: ", thead.text)
web_Table = chdriver.find_element(By.XPATH, "//table[@id='sampleTable']/thead")
column = web_Table.find_element(By.TAG_NAME, "tr")
# //*[@id="sampleTable"]/thead/tr
# //*[@id="sampleTable"]/thead/tr/th[1]
# //*[@id="sampleTable"]/thead/tr/th[2]
for col in column:
    col_value = col.find_elements(By.TAG_NAME, "th")
    print(col_value)
# //*[@id="sampleTable"]/thead/tr
# //*[@id="sampleTable"]/thead/tr/th[1]
# //*[@id="sampleTable"]/thead/tr/th[2]

# webtable = chdriver.find_element(By.XPATH, '//table[@id="sampleTable"]/tbody')
# rows = webtable.find_elements(By.TAG_NAME, "tr")
#
# for rw in rows:
#     cells = rw.find_elements(By.TAG_NAME, "td")
#     for cell in cells:
#         print(cell.text," ",end="")
#     print()
# time.sleep(10)
# time.sleep(10)