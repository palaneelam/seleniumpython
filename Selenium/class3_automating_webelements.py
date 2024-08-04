import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

URL = "https://edwheel.com/index.php/selenium-practice/"

def launchbrowser(browsername):
    if browsername =='chrome':
        driver = webdriver.Chrome()
        return driver
    else:
        print("Wrong Browser")
        return "none"

def openApplication(driver, url):
    driver.get(url)
    driver.maximize_window()


chdriver = launchbrowser('chrome')
openApplication(chdriver, URL)

# chdriver.find_element(By.LINK_TEXT, "Sample Link")
# chdriver.find_element(By.PARTIAL_LINK_TEXT, "Sample").click()

chdriver.find_element(By.ID, "countrySuggestion").send_keys("Australia")

text_link = chdriver.find_element(By.LINK_TEXT, "Sample Link").text
print("text on the link: ",text_link)

# text_autosuggestion = chdriver.find_element(By.ID, "countrySuggestion").text
# text_autosuggestion = chdriver.find_element(By.ID, "countrySuggestion").get_attribute("value")
# chdriver.find_element(By.ID, "countrySuggestion").send_keys("A")
# try:
#     chdriver.find_element(By.CSS_SELECTOR, "#countrySuggestion > option:first-child").click()
# except:
#     time.sleep(15)
# print("Link on the autosuggestion: ",text_autosuggestion)

# chdriver.find_element(By.XPATH, '//button[text()="Alert"]').click()
# alertbox = chdriver.switch_to.alert
# print("Text on alert box is:",alertbox.text)
# alertbox.accept()
#
# chdriver.find_element(By.XPATH, '//button[text()="Confirm"]').click()
# confirmbox = chdriver.switch_to.alert
# print("Text on alert box is:",confirmbox.text)
# time.sleep(5)
# confirmbox.dismiss()

# chdriver.find_element(By.XPATH, '//button[@id="switchWindowButton"][1]').click()
# print("Original Page:",chdriver.title)
# # chdriver.switch_to.
# print("After switching Page:",chdriver.title)


# calendar = chdriver.find_element(By.ID, "calendarInput")
# calendar.send_keys("08/04/2024")

# time.sleep(5)
# des_date = "05"
# calendar = chdriver.find_element(By.XPATH, f"//a[text()='{des_date}']").click()

# webtable = chdriver.find_element(By.XPATH, '//table[@id="sampleTable"]/tbody')
# rows = webtable.find_elements(By.TAG_NAME, "tr")
#
# for rw in rows:
#     cells = rw.find_elements(By.TAG_NAME, "td")
#     for cell in cells:
#         print(cell.text," ",end="")
#     print()
# time.sleep(10)
#
# print("Original Page:",chdriver.title)
# chdriver.find_element(By.ID, "toggleIframeButton").click()
# time.sleep(5)
# chdriver.switch_to.frame("exampleIframe")
# text_toread = chdriver.find_element(By.XPATH, '//section[@id="selenium-with-python"]/dl/dt[1]').text
# print("After clicking iframe Page:",text_toread)
# chdriver.switch_to.default_content()
# print("After coming out of frame:",chdriver.title)


original_window = chdriver.current_window_handle
# print("Original window:", original_window)
chdriver.find_element(By.ID, 'switchTabButton').click()
for hndle in chdriver.window_handles:
    print("New window:", hndle)
    if original_window != hndle:
        chdriver.switch_to.window(hndle)
        break

print("switched window title:",chdriver.title)
chdriver.switch_to.window(original_window)
print("after reverting window title:",chdriver.title)













