import time

from selenium.webdriver.support.select import Select

from Demo_Ecommerce.Functional_Libraries.common_libraries import wait_for_visibility_of_element_classname, \
 wait_for_visibility_of_element_xpath
from Demo_Ecommerce.object_repository.testcase1_objects import page_title_name, mobileMenu, sortwindowxpath


#Step 2 Get the Titile of the Page
def geting_pageTitle(driver):
 element1=wait_for_visibility_of_element_classname(driver,page_title_name)
 title=element1.text
 print(title)
 time.sleep(20)

#Step 3 Click on the Mobile Menu and navigate to next page
def click_mobile_menu(driver):
 element2=wait_for_visibility_of_element_xpath(driver,mobileMenu)
 element2.click()

#step 4 Verify the TItle of the Page is Mobile
def getting_subpage_title(driver):
 element3=driver.title
 print(element3)
 time.sleep(20)

#step 5 Select name from Sort By Dropdown and validate mobiles are sorting by name.
def sort_by_name(driver):
 element4=Select(wait_for_visibility_of_element_xpath(driver,sortwindowxpath))
 element4.select_by_index(1)
 time.sleep(10)
















