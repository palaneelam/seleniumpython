# Hard coded wait statements / Static wait statement
    # Implicit wait statement
    # time.sleep
# Explicit wait statement - is not a hard coded wait statement | Dynamic wait statement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://edwheel.com/index.php/selenium-practice/")
driver.maximize_window()

# Explicit
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.ID, "name"))).send_keys("Neelam P")

print("explicit statement")

#** capturing screenshot

# driver.save_screenshot("full_page_ss.png")

textbox = driver.find_element(By.ID, "name")
textbox.screenshot(r"C:\\EdWheel\\name_ss_1.jpg")
# textbox.screenshot_as_png("name_ss_new")






















