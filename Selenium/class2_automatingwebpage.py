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

chdriver.find_element(By.ID, "name").send_keys("Neelam")
chdriver.find_element(By.ID, "email").send_keys("neelam@testautomationcoach.com")

chdriver.find_element(By.XPATH,"//button[text()='Reset Dummy Button']").click()
chdriver.find_element(By.ID,"chbValue1").click()

chkbox = chdriver.find_element(By.ID,"chbValue2")
chkbox.click()

dropdwn = chdriver.find_element(By.ID,"dropdown")
selct_dp_value = Select(dropdwn)
selct_dp_value.select_by_value("DPValue1")
selct_dp_value.select_by_index(2)
selct_dp_value.select_by_visible_text("DPValue 3")

lisbox = chdriver.find_element(By.ID,"listbox")
selct_listbox_value = Select(lisbox)
selct_listbox_value.select_by_value("list1")
time.sleep(5)
selct_listbox_value.select_by_index(1)
time.sleep(5)
selct_listbox_value.select_by_visible_text("List 3")
time.sleep(10)















