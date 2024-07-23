import time

from selenium import webdriver

from Demo_Ecommerce.config.test_setting import TestSettings
from Demo_Ecommerce.page_objects.testcase_1_scenarios import click_mobile_menu
from Demo_Ecommerce.page_objects.testcase_4_scenario import comparemob
from Demo_Ecommerce.page_objects.testcase_5_scenario import newAcc


class Tests:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.main_page_url
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)

    def run_test_case5(self):
        newAcc(self.driver)
        time.sleep(5)


tests = Tests()
tests.run_test_case5()
tests.driver.quit()




