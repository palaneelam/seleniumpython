import time

from selenium import webdriver

from Demo_Ecommerce.config.test_setting import TestSettings
from Demo_Ecommerce.page_objects.testcase_1_scenarios import click_mobile_menu
from Demo_Ecommerce.page_objects.testcase_4_scenario import comparemob


class Tests:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.main_page_url
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
    def run_test_case4(self):
        click_mobile_menu(self.driver)
        time.sleep(2)
        comparemob(self.driver)
        time.sleep(2)

tests = Tests()
tests.run_test_case4()
tests.driver.quit()