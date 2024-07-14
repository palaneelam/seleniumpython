import time

from Demo_Ecommerce.Functional_Libraries.common_libraries import wait_for_visibility_of_element_xpath, \
    wait_for_visibility_of_element_linktext
from Demo_Ecommerce.object_repository.testcase2_objects import mobprice1, link2, mobprice2


def price_comparision(driver):
    driver.execute_script("window.scrollBy(0,300)"," ")
    element1=wait_for_visibility_of_element_xpath(driver,mobprice1)
    price1=element1.text
    time.sleep(2)
    #clink the mobile link to open the detail page
    element2=wait_for_visibility_of_element_xpath(driver,link2)
    element2.click()
    time.sleep(3)
    #get the mobile price from Detail page
    element3=wait_for_visibility_of_element_xpath(driver,mobprice2)
    price2=element3.text
    time.sleep(3)
    #Compare the Prices and print the Price
    if(price1==price2):
        print("The Price of the Mobile is ", price1)
    else :
        print("The Price is different")
