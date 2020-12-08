import time
from selenium import webdriver

# Chrome Driver initialization
driver = webdriver.Chrome()

# Pause 5 seconds
time.sleep(5)

# Open url with site
driver.get('https://stepik.org/lesson/25969/step/12')
time.sleep(5)

# Find and send text to textarea
textarea = driver.find_element_by_css_selector('.textarea')
textarea.send_keys('get()')
time.sleep(5)

# Find and click on submit button
submit_button = driver.find_element_by_css_selector('.submit-submission')
submit_button.click()
time.sleep(5)

driver.quit()