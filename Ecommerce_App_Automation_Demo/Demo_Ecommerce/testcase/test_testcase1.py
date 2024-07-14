import time

from selenium import webdriver

from Demo_Ecommerce.config.test_setting import TestSettings
from Demo_Ecommerce.page_objects.testcase_1_scenarios import geting_pageTitle, click_mobile_menu, getting_subpage_title, \
    sort_by_name


#step 1 launch the url
class Tests:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.main_page_url
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
    def run_test_to_get_Title(self):
        geting_pageTitle(self.driver)
        time.sleep(10)
        click_mobile_menu(self.driver)
        time.sleep(2)
        getting_subpage_title(self.driver)
        time.sleep(10)
        sort_by_name(self.driver)
        time.sleep(5)
tests = Tests()
tests.run_test_to_get_Title()
tests.driver.quit()