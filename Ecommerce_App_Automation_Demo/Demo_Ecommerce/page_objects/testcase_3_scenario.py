import time

from Demo_Ecommerce.Functional_Libraries.common_libraries import wait_for_visibility_of_element_xpath
from Demo_Ecommerce.object_repository.testcase3_objects import addtocart, qtybox, updatebutton, error_text1, emptycart, \
    emptymessage


def error_message_verification(driver):
    driver.execute_script("window.scrollBy(0,300)"," ")
    element1=wait_for_visibility_of_element_xpath(driver,addtocart)
    element1.click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,200)", " ")
    box=wait_for_visibility_of_element_xpath(driver,qtybox)
    box.send_keys("1000")
    time.sleep(3)
    updatebtn=wait_for_visibility_of_element_xpath(driver,updatebutton)
    updatebtn.click()
    error_txt_verification=wait_for_visibility_of_element_xpath(driver,error_text1)
    Message=error_txt_verification.text
    if(Message=="* The maximum quantity allowed for purchase is 500."):
       print(Message)
    else:
        print("Opps it is wrong sorry!!!!")
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,200)", " ")
    emptycrt=wait_for_visibility_of_element_xpath(driver,emptycart)
    emptycrt.click()
    time.sleep(3)
    confmessage=wait_for_visibility_of_element_xpath(driver,emptymessage)
    message_confirmation=confmessage.text
    print(message_confirmation)
    time.sleep(6)