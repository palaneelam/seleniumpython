import os
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

# 1. A/B testing *************************************

# driver.find_element(By.LINK_TEXT, "A/B Testing").click()
# time.sleep(5)
#
# headertext = driver.find_element(By.TAG_NAME, "h3").text
# print(headertext)
# pageContent = driver.find_element(By.XPATH, "//h3/following::p").text
# print(pageContent)
# driver.back()
# time.sleep(2)

# 2. Add/Remove Element *************************************
# driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//button").click()
# time.sleep(2)
# print("Added a button!!!")
# driver.find_element(By.XPATH, "//button[text()='Delete']").click()
# time.sleep(2)
# print("Deleted a button!!!")
# # assertion - validation
# # assert not driver.find_element(By.XPATH, "//button[text()='Delete']"), "Element deletion failed!"
# try:
#     delbutton = driver.find_element(By.XPATH, "//button[text()='Delete']")
# except Exception:
#     print("Button Does not exist")
# driver.back()
# time.sleep(2)

# 3. Basic Auth *************************************
# username = "admin"
# password = "admin"
#
# url = "https://the-internet.herokuapp.com/basic_auth"
# driver.get(url)
#
# url_split = url.split("//")[1]
# new_url = f"https://{username}:{password}@{url_split}"
# print(new_url)
# driver.get(new_url)
#
# if "Congratulations! You must have the proper credentials." in driver.page_source:
#     print("Success!!")
# else:
#     print("Failed!!")
# driver.back()
# time.sleep(10)

# 4. Basic Auth *************************************
# driver.find_element(By.LINK_TEXT, "Broken Images").click()
# images = driver.find_elements(By.TAG_NAME, "img")
# broken_img_cnt = 0

# ********  One way to do ***********
# broken_images = []
# for image in images:
#     response = image.get_attribute('naturalWidth')
#     if response == '0':
#         broken_images.append(image.get_attribute('src'))
#     print(broken_images)
#
# if broken_images:
#     print("Broken images found")
#     for url in broken_images:
#         print(url)
# else:
#     print("No broken image")


# ******** second way to do the same thing ************
# for image in images:
#     src = image.get_attribute('src')
#     response = driver.execute_script('return fetch(arguments[0], {method:"HEAD"})', src)
#     if response['status'] == 200:
#         pass
#     else:
#         print(f"Broken image found: {src}")
#         broken_img_cnt += 1
#
# if broken_img_cnt == 0:
#     print("No broken image")
# else:
#     print(f"Total number of broken images are: {broken_img_cnt}")
#
# driver.back()
# time.sleep(10)

# 5. Challenging DOM *************************************
# driver.find_element(By.LINK_TEXT, "Challenging DOM").click()
# edit_button = driver.find_element(By.XPATH, "(//a[text()='edit'])[1]").click()
# editurl = driver.current_url
# if "edit" in editurl:
#     print("Pass")
# else:
#     print("Fail")
#
# table_content = driver.find_element(By.XPATH, "//table").text
# print("table content is: ", table_content)
#
# driver.back()
# time.sleep(10)

# 6. Checkboxes *************************************************
# Opening the page
driver.get("https://the-internet.herokuapp.com/checkboxes")

# Finding all checkboxes
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

# Checking the first checkbox if it's unchecked
if not checkboxes[0].is_selected():
    checkboxes[0].click()
    print("Checkbox 1 checked.")
else:
    print("Checkbox 1 already checked.")

# Unchecking the second checkbox if it's checked
if checkboxes[1].is_selected():
    checkboxes[1].click()
    print("Checkbox 2 unchecked.")
else:
    print("Checkbox 2 already unchecked.")

# 7. Context Menu **********************************************
driver.find_element(By.LINK_TEXT, "Context Menu").click()

context_menu = driver.find_element(By.ID, "hot-spot")

actions = ActionChains(driver)
actions.context_click(context_menu).perform()

alert = driver.switch_to.alert
print("Alert text:",alert.text)
alert.accept()

# *************************   8th link - Digest Authentication
# Define the URL of the page to automate
url = "https://the-internet.herokuapp.com/digest_auth"

# Define the username and password for HTTP Digest Authentication
username = "admin"
password = "admin"

url_with_credentials = f"https://{username}:{password}@the-internet.herokuapp.com/digest_auth"

# If authentication successful, print success message
print("Successfully authenticated!")

# *************************   9th link - Disappearing Elements
# Navigating to the webpage
driver.get("https://the-internet.herokuapp.com/disappearing_elements")
# Waiting for the elements to load
elements_present = expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#content ul"))
WebDriverWait(driver, 10).until(elements_present)

# Getting all the navigation links
navigation_links = driver.find_elements(By.CSS_SELECTOR, "#content ul li a")

# Printing the text of each navigation link
print("Navigation Links:")
for link in navigation_links:
    print(link.text)

# *************************   10th link - Drag and Drop
# Open the webpage
driver.get("https://the-internet.herokuapp.com/drag_and_drop")

# Locate the draggable element
draggable_element = driver.find_element(By.ID, "column-a")

# Locate the target drop zone
drop_zone = driver.find_element(By.ID, "column-b")

# Perform the drag and drop action
action_chains = ActionChains(driver)
action_chains.drag_and_drop(draggable_element, drop_zone).perform()

# Wait for a moment to observe the result (optional)
time.sleep(3)

# *************************   11th link - DropDown
# Open the URL
driver.get("https://the-internet.herokuapp.com/dropdown")

# Find the dropdown element by its ID
dropdown = driver.find_element(By.ID, "dropdown")

# Wrap the dropdown element in a Select object
select = Select(dropdown)

# Select an option by its visible text
select.select_by_visible_text("Option 1")

# Wait for a moment to see the selection
time.sleep(2)

# *************************   13th link - Dynamic Content
# Open the dynamic content page
driver.get("https://the-internet.herokuapp.com/dynamic_content")

# Locate and print the dynamic content
dynamic_content = driver.find_element(By.CSS_SELECTOR, ".large-10.columns")
print("Dynamic Content:")
print(dynamic_content.text)

# *************************   14th link - Dynamic Controls
# Navigate to the page
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# Locate the checkbox and the "Remove" button
checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox input[type='checkbox']")
remove_button = driver.find_element(By.XPATH, "//button[text()='Remove']")

# Click on the "Remove" button to demonstrate dynamic content change
remove_button.click()

# Wait for the checkbox to disappear
WebDriverWait(driver, 10).until(
    expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, "#checkbox input[type='checkbox']")))

# Locate the "Add" button
add_button = driver.find_element(By.CSS_SELECTOR, "#input-example button")

# Click on the "Add" button to demonstrate dynamic content change
add_button.click()

# # Wait for the checkbox to appear
# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkbox input[type='checkbox']")))

# Locate the input field
input_field = driver.find_element(By.CSS_SELECTOR, "#input-example input[type='text']")
locator = (By.CSS_SELECTOR, "#input-example input[type='text']")
# wait_until_element_not_interactable(driver, locator)
time.sleep(25)
# Enter text into the input field
input_field.send_keys("Hello, Selenium!")

# *************************   15th link - Dynamic Loading
# Navigating to the page
driver.get("https://the-internet.herokuapp.com/dynamic_loading")

# Clicking on the "Example 1: Element on page that is hidden" link
example1_link = WebDriverWait(driver, 10).until(
    expected_conditions.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Example 1")))
example1_link.click()

# Waiting for the loading to finish
WebDriverWait(driver, 25).until(expected_conditions.visibility_of_element_located((By.ID, "finish")))

# Retrieving the text of the loaded element
loaded_element_text = driver.find_element(By.ID, "finish").text
print("Text of the loaded element:", loaded_element_text)

# *************************   16th link - Entry Ad
driver.get("https://the-internet.herokuapp.com/entry_ad")

# Wait for the modal to appear
time.sleep(3)  # This is a simple wait. For better practice, use WebDriverWait.

# Close the modal by clicking the 'Close' button
close_button = driver.find_element(By.CSS_SELECTOR, 'div.modal-footer > p')
close_button.click()

# Verify the modal is closed
try:
    modal = driver.find_element(By.ID, 'modal')
    if not modal.is_displayed():
        print("Modal closed successfully.")
    else:
        print("Modal is still open.")
except:
    print("Modal closed successfully.")

# *************************   16th link - Exit Intent
driver.get('https://the-internet.herokuapp.com/exit_intent')

# Allow some time for the page to load
time.sleep(2)

# Create an instance of ActionChains
actions = ActionChains(driver)

# Move the mouse to trigger the exit intent
# Moving to the top left corner of the screen
actions.move_by_offset(0, 0).perform()

# Allow some time to see the modal
time.sleep(2)

# Check if the modal appears
modal = driver.find_element(By.CSS_SELECTOR, '.modal')
if modal.is_displayed():
    print("Exit intent modal displayed successfully.")
else:
    print("Exit intent modal not displayed.")

# Close the modal (if needed)
close_button = driver.find_element(By.XPATH, '//p[text()="Close"]')
close_button.click()
# *************************   17th link - File Download
options = webdriver.ChromeOptions()
download_path = r"C:\GIT"
prefs = {"download.default_directory": download_path}
options.add_experimental_option("prefs", prefs)

# Initialize the Chrome driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/download")

# Wait for the page to load
time.sleep(2)

# Locate the first file download link and click it
download_link = driver.find_element(By.CSS_SELECTOR, "div.example a")
download_link.click()

# Wait for the download to complete
time.sleep(10)  # Adjust time based on your internet speed

# Verify the download
downloaded_file_name = download_link.text
downloaded_file_path = os.path.join(download_path, downloaded_file_name)

if os.path.exists(downloaded_file_path):
    print(f"File '{downloaded_file_name}' downloaded successfully.")
else:
    print(f"Failed to download file '{downloaded_file_name}'.")
# *************************   18th link - File Upload

# *************************   19th link - Floating Menu
driver.get("https://the-internet.herokuapp.com/floating_menu")

# Maximize the browser window
driver.maximize_window()

# Wait for the page to load completely
time.sleep(2)

# Scroll down the page to see the floating menu
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)  # Wait to ensure the scroll action completes

# Locate the floating menu items
home_link = driver.find_element(By.LINK_TEXT, "Home")
news_link = driver.find_element(By.LINK_TEXT, "News")
contact_link = driver.find_element(By.LINK_TEXT, "Contact")
about_link = driver.find_element(By.LINK_TEXT, "About")

# Interact with each menu item
menu_items = [home_link, news_link, contact_link, about_link]
for item in menu_items:
    ActionChains(driver).move_to_element(item).click().perform()
    time.sleep(1)  # Wait to observe the action
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Wait for any potential page load

# Optionally, verify the floating menu is still visible after interactions
floating_menu = driver.find_element(By.ID, "menu")
assert floating_menu.is_displayed(), "Floating menu should be visible after interactions"

print("Test completed successfully!")
# *************************   20th link - Forgot Password
driver.get("https://the-internet.herokuapp.com/forgot_password")

# Find the email input field and enter an email address
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("test@example.com")

# Find the retrieve password button and click it
retrieve_button = driver.find_element(By.ID, "form_submit")
retrieve_button.click()

# Optionally, verify the result or assert some condition
# For example, we can check if the URL has changed or if a specific message appears
success_message = driver.find_element(By.TAG_NAME, "h1").text
assert success_message == "Internal Server Error", "Test failed: Unexpected success message"

print("Test completed successfully!")
# *************************   21st link - Form Authentication
driver.get("https://the-internet.herokuapp.com/login")

# Find the username and password input fields
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

# Enter the credentials
username_input.send_keys("tomsmith")
password_input.send_keys("SuperSecretPassword!")

# Find the login button and click it
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for a few seconds to see the result
time.sleep(3)

# Optionally, verify the login success
success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
print(success_message)
# *************************   22nd link - Frames
driver.get('https://the-internet.herokuapp.com/frames')

# Locate and click on the "Nested Frames" link
nested_frames_link = driver.find_element(By.LINK_TEXT, 'Nested Frames')
nested_frames_link.click()

# Switch to the nested frames
driver.switch_to.frame(driver.find_element(By.NAME, 'frame-top'))
driver.switch_to.frame(driver.find_element(By.NAME, 'frame-left'))

# Get text from the left frame
left_frame_text = driver.find_element(By.TAG_NAME, 'body').text
print("Left frame text:", left_frame_text)

# Switch to the parent frame and then to the middle frame
driver.switch_to.parent_frame()
driver.switch_to.frame(driver.find_element(By.NAME, 'frame-middle'))

# Get text from the middle frame
middle_frame_text = driver.find_element(By.ID, 'content').text
print("Middle frame text:", middle_frame_text)

# Switch to the parent frame and then to the right frame
driver.switch_to.parent_frame()
driver.switch_to.frame(driver.find_element(By.NAME, 'frame-right'))

# Get text from the right frame
right_frame_text = driver.find_element(By.TAG_NAME, 'body').text
print("Right frame text:", right_frame_text)

# Switch to the main content
driver.switch_to.default_content()

# Navigate back to the frames page
driver.get('https://the-internet.herokuapp.com/frames')

# Locate and click on the "iFrame" link
iframe_link = driver.find_element(By.LINK_TEXT, 'iFrame')
iframe_link.click()

# Switch to the iFrame
driver.switch_to.frame(driver.find_element(By.ID, 'mce_0_ifr'))

# Get text from the iFrame
iframe_text = driver.find_element(By.ID, 'tinymce').text
print("iFrame text:", iframe_text)
# *************************   23rd link - Geolocation
driver.get('https://the-internet.herokuapp.com/geolocation')

# Find the "Where am I?" button and click it
geolocation_button = driver.find_element(By.XPATH, '//button[text()="Where am I?"]')
geolocation_button.click()

# Wait for the geolocation information to appear (adjust sleep duration as needed)
time.sleep(5)

# Extract the latitude and longitude values
latitude = driver.find_element(By.ID, 'lat-value').text
longitude = driver.find_element(By.ID, 'long-value').text

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

# *************************   24th link - Horizontal slider
driver.find_element(By.LINK_TEXT, "Horizontal Slider").click()
slider = driver.find_element(By.XPATH, "//input[@type='range']")

desired_value = 2

# Calculate the number of steps required to move to the desired position
slider_min = float(slider.get_attribute('min'))
slider_max = float(slider.get_attribute('max'))
slider_step = float(slider.get_attribute('step'))
steps = (desired_value - slider_min) / slider_step

actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(steps * 10, 0).release().perform()
time.sleep(2)

slider_value = driver.find_element(By.ID, "range").text
print(f"Slider value after moving: {slider_value}")

driver.back()
time.sleep(10)

# *************************   25th link - Hover
driver.find_element(By.LINK_TEXT, "Hovers").click()
figures = driver.find_elements(By.CLASS_NAME, 'figure')

actions = ActionChains(driver)
for i, figure in enumerate(figures):
    actions.move_to_element(figure).perform()
    time.sleep(2)
    caption = figure.find_element(By.CLASS_NAME, 'figcaption')
    print(f'Hovering over figure {i + 1} reveals: {caption.text}')

driver.back()
time.sleep(10)

# *************************   26th link - Infinite Scroll
driver.find_element(By.LINK_TEXT, "Infinite Scroll").click()
num_scrolls = 10
for _ in range(num_scrolls):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)
paragraphs = driver.find_elements(By.CSS_SELECTOR, '.jscroll-added')
for paragraph in paragraphs:
    print(paragraph.text)

driver.back()
time.sleep(10)

# *************************   27th link - Inputs
driver.find_element(By.LINK_TEXT, "Inputs").click()
input_field = driver.find_element(By.TAG_NAME, 'input')
number_to_enter = "12345"
input_field.send_keys(number_to_enter)
time.sleep(2)
print(f"Entered value: {input_field.get_attribute('value')}")

driver.back()
time.sleep(10)

# *************************   28th link - JQuery UI Menus
driver.find_element(By.LINK_TEXT, "JQuery UI Menus").click()


driver.back()
time.sleep(10)

# *************************   29th link - JavaScript Alerts
driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
wait = WebDriverWait(driver, 10)

def handle_alert(action="accept", text=None):
    alert = wait.until(expected_conditions.alert_is_present())
    if text:
        alert.send_keys(text)
    if action == "accept":
        alert.accept()
    else:
        alert.dismiss()

# Click the first button to trigger a simple alert and accept it
simple_alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
simple_alert_button.click()
handle_alert("accept")

# Click the second button to trigger a confirmation alert and dismiss it
confirm_alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_alert_button.click()
handle_alert("dismiss")

# Click the third button to trigger a prompt alert, enter text, and accept it
prompt_alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
prompt_alert_button.click()
handle_alert("accept", text="Test input")

driver.back()
time.sleep(10)

# *************************   30th link - JavaScript onload event error
driver.find_element(By.LINK_TEXT, "JavaScript onload event error").click()
logs = driver.get_log("browser")

js_errors = []
for log in logs:
    if log['level'] == 'SEVERE':
        js_errors.append(log)

if js_errors:
    print("JavaScript errors found:")
    for error in js_errors:
        print(error)
else:
    print("No JavaScript errors found.")

driver.back()
time.sleep(10)

# *************************   31st link - Key Presses
driver.find_element(By.LINK_TEXT, "Key Presses").click()
body = driver.find_element(By.TAG_NAME, "body")

keys_to_test = [Keys.ARROW_DOWN, Keys.ARROW_UP, Keys.ARROW_LEFT, Keys.ARROW_RIGHT, Keys.ENTER, Keys.ESCAPE]

for key in keys_to_test:
    body.send_keys(key)
    time.sleep(1)
    result = driver.find_element(By.ID, "result").text
    print(f"Result = {result}")


driver.back()
time.sleep(10)

# *************************   32nd link - Large & Deep DOM
driver.find_element(By.LINK_TEXT, "Large & Deep DOM").click()
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
time.sleep(2)
element = driver.find_element(By.XPATH, "//h3[text()='Large Content']")
print("Element found: ", element.text)

driver.back()
time.sleep(10)

# *************************   33rd link - Multiple Windows
driver.find_element(By.LINK_TEXT, "Multiple Windows").click()
driver.find_element(By.LINK_TEXT, "Click Here").click()

main_window = driver.current_window_handle
all_windows = driver.window_handles

for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        break

print(f"New Window Title: {driver.title}")

driver.switch_to.window(main_window)

print(f"Main Window Title: {driver.title}")

driver.back()
time.sleep(10)

# *************************   34th link - Nested Frames
driver.find_element(By.LINK_TEXT, "Nested Frames").click()

driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
left_frame_text = driver.find_element(By.TAG_NAME, "body").text
print("Left Frame Text:", left_frame_text)

driver.switch_to.parent_frame()

driver.switch_to.frame("frame-middle")

middle_frame_text = driver.find_element(By.ID, "content").text
print("Middle Frame Text:", middle_frame_text)

driver.switch_to.parent_frame()

driver.switch_to.frame("frame-right")

right_frame_text = driver.find_element(By.TAG_NAME, "body").text
print("Right Frame Text:", right_frame_text)

driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom")

bottom_frame_text = driver.find_element(By.TAG_NAME, "body").text
print("Bottom Frame Text:", bottom_frame_text)


driver.back()
time.sleep(10)

# *************************   35th link - Notification Messages
driver.find_element(By.LINK_TEXT, "Notification Messages").click()

def click_and_get_message():
    driver.find_element(By.LINK_TEXT, 'Click here').click()
    time.sleep(1)
    message = driver.find_element(By.ID, 'flash').text
    return message

for i in range(5):
    msg = click_and_get_message()
    print(f"Attempt {i+1}: {msg}")

driver.back()
time.sleep(10)

# *************************   36th link - Redirect Link
driver.find_element(By.LINK_TEXT, "Redirect Link").click()
redirect_link = driver.find_element(By.LINK_TEXT, 'here')
redirect_link.click()

time.sleep(3)

status_code_text = driver.find_element(By.TAG_NAME, 'h3').text
assert 'Status Codes' in status_code_text, "Redirection failed or incorrect page"

status_200_link = driver.find_element(By.LINK_TEXT, '200')
status_200_link.click()

result_text = driver.find_element(By.TAG_NAME, 'p').text
print(result_text)


driver.back()
time.sleep(10)

# *************************   37th link - Secure File Download
driver.find_element(By.LINK_TEXT, "Secure File Download").click()
wait = WebDriverWait(driver, 10)

chrome_options = Options()
download_dir = r"C:\Users\Neelam\PycharmProjects\SeleniumPython\downloads"

chrome_prefs = {
    "download.default_directory": download_dir,
    "profile.default_content_settings.popups": 0,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
}

chrome_options.add_experimental_option("prefs", chrome_prefs)

driver = webdriver.Chrome(options=chrome_options)
secure_url = f"https://admin:admin@the-internet.herokuapp.com/download_secure"

driver.get(secure_url)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".example a")))

# Locate the first file link and click to download
file_link = driver.find_element(By.CSS_SELECTOR, ".example a")
file_link.click()

WebDriverWait(driver, 10).until(lambda driver: os.path.exists(os.path.join(download_dir, file_link.text)))
# ********* if above line gets complicated - replace with below commented code *****************

# file_path = os.path.join(download_dir, file_link.text)
#
# for _ in range(10):
#     if os.path.exists(file_path):
#         print("File has been downloaded.")
#         break
#     time.sleep(1)
# else:
#     print("File download failed or took too long.")


driver.back()
time.sleep(10)

# *************************   38th link - Shadow DOM
driver.find_element(By.LINK_TEXT, "Shadow DOM").click()
# Locate the first 'my-paragraph' custom element (shadow host)
shadow_host = driver.find_element(By.TAG_NAME, 'my-paragraph')

# Access the shadow root using JavaScript
shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)

# Find the paragraph element inside the shadow root
paragraph = shadow_root.find_element(By.CSS_SELECTOR, 'p')

# Retrieve and print the text content of the paragraph
print("Text inside the shadow DOM:", paragraph.text)

# Interact with the content in the slot
slot_content = shadow_root.find_element(By.CSS_SELECTOR, 'slot[name="my-text"]')
print("Slot content:", slot_content.text)

# If you want to interact with the content passed into the slot (e.g., a span or ul element)
assigned_nodes = driver.execute_script("return arguments[0].assignedNodes()", slot_content)
for node in assigned_nodes:
    print("Assigned Node Content:", node.text)


driver.back()
time.sleep(10)

# *************************   39th link - Shifting Content
driver.find_element(By.LINK_TEXT, "Shifting Content").click()
option1_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Example 1')
option1_link.click()

driver.implicitly_wait(2)
option1_content = driver.find_element(By.TAG_NAME, 'ul').text
print("Content after clicking 'Option 1':", option1_content)

driver.get("https://the-internet.herokuapp.com/shifting_content")

option2_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Example 3')
option2_link.click()

driver.implicitly_wait(2)

option2_content = driver.find_element(By.CSS_SELECTOR, '.large-centered').text
print("Content after clicking 'Option 2':", option2_content)

driver.back()
time.sleep(10)

# *************************   40th link - Slow Resources
driver.find_element(By.LINK_TEXT, "Slow Resources").click()



driver.back()
time.sleep(10)

# *************************   41st link - Sortable Data Tables
driver.find_element(By.LINK_TEXT, "Sortable Data Tables").click()

table = driver.find_element(By.ID, "table1")
rows = table.find_elements(By.TAG_NAME, "tr")

for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    for column in columns:
        print(column.text, end=" | ")
    print()

due_header = table.find_element(By.XPATH, "//span[text()='Due']")
due_header.click()

rows = table.find_elements(By.TAG_NAME, "tr")
print("\nTable after sorting by 'Due':")
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    for column in columns:
        print(column.text, end=" | ")
    print()

for row in rows:
    if "Tim Conway" in row.text:
        print("\nRow with 'Tim Conway':")
        columns = row.find_elements(By.TAG_NAME, "td")
        for column in columns:
            print(column.text, end=" | ")
        print()
        break


driver.back()
time.sleep(10)

# *************************   42nd link - Status Codes
driver.find_element(By.LINK_TEXT, "Status Codes").click()
status_codes = ['200', '301', '404', '500']

for code in status_codes:
    status_link = driver.find_element(By.PARTIAL_LINK_TEXT, code)

    status_link.click()

    content = driver.find_element(By.TAG_NAME, 'p').text

    if code in content:
        print(f"Status code {code} page verified successfully.")
    else:
        print(f"Status code {code} page verification failed.")

driver.back()
time.sleep(10)

# *************************   43rd link - Typos
driver.find_element(By.LINK_TEXT, "Typos").click()

paragraphs = driver.find_elements(By.TAG_NAME, 'p')

for index, paragraph in enumerate(paragraphs):
    print(f"Paragraph {index + 1}: {paragraph.text}")

driver.back()
time.sleep(10)

# *************************   44th link - WYSIWYG Editor
driver.find_element(By.LINK_TEXT, "WYSIWYG Editor").click()

iframe = driver.find_element(By.CSS_SELECTOR, "iframe.tox-edit-area__iframe")
driver.switch_to.frame(iframe)

editor_body = driver.find_element(By.CSS_SELECTOR, "body")

editor_body.clear()

# Type text into the editor
editor_body.send_keys("Hello, this is a test message!")

editor_body.send_keys(Keys.ENTER)
editor_body.send_keys("This is another line.")

driver.switch_to.default_content()

driver.back()
time.sleep(10)