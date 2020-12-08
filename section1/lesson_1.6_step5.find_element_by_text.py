from selenium import webdriver
import time
import math

# Link to tested site on git and browser initialization
link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()

try:
    # Open tested site
    browser.get(link)
    time.sleep(3)

    # Find hidden link
    text_link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    text_link.click()

    # Fill out the registration form
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    # Find button for confirm and send data
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

