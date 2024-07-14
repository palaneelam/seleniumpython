import time

from Demo_Ecommerce.Functional_Libraries.common_libraries import wait_for_visibility_of_element_xpath
from Demo_Ecommerce.object_repository.testcase4_objects import compare1mob, compare2mob, comparebutton, clw


def comparemob(driver):
    driver.execute_script("window.scrollBy(0,300)"," ")
    time.sleep(30)
    compare1cart=wait_for_visibility_of_element_xpath(driver,compare1mob)
    compare1cart.click()
    compare2cart=wait_for_visibility_of_element_xpath(driver,compare2mob)
    compare2cart.click()
    comparbutton=wait_for_visibility_of_element_xpath(driver,comparebutton)
    comparbutton.click()
    time.sleep(2)
    windowh=driver.window_handles
    driver.switch_to.window(windowh[1])
    driver.execute_script("window.scrollBy(0,250)", " ")
    time.sleep(10)
    close=wait_for_visibility_of_element_xpath(driver,clw)
    close.click()
   # time.sleep(4)