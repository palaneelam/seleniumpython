import time

from Demo_Ecommerce.Functional_Libraries.common_libraries import wait_for_visibility_of_element_xpath, \
    wait_for_visibility_of_element_linktext
from Demo_Ecommerce.object_repository.testcase5_objects import account, registerA, firstnametextbox, lastnamebox, \
    passwordbox, confirmpasswordbox, emailbox, Register_button


class TVlink:
    pass


def newAcc(driver):
    Account = wait_for_visibility_of_element_xpath(driver, account)
    Account.click()
    Registration=wait_for_visibility_of_element_linktext(driver,registerA)
    Registration.click()
    firstnamebox=wait_for_visibility_of_element_xpath(driver,firstnametextbox)
    firstnamebox.send_keys("Munia")
    lastnamebx = wait_for_visibility_of_element_xpath(driver, lastnamebox)
    lastnamebx.send_keys("RoyC")
    pswd = wait_for_visibility_of_element_xpath(driver, passwordbox )
    pswd.send_keys("1234567")
    cpswd = wait_for_visibility_of_element_xpath(driver, confirmpasswordbox)
    cpswd.send_keys("1234567")
    emailbx = wait_for_visibility_of_element_xpath(driver, emailbox)
    emailbx.send_keys("munia.royc1@gmail.com")
    registerbtn = wait_for_visibility_of_element_xpath(driver, Register_button)
    registerbtn.click()
    time.sleep(6)
    tl= wait_for_visibility_of_element_linktext(driver,TVlink)
    tl.click()
    time.sleep(8)
