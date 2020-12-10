from selenium import webdriver
import math
import time

# Site link
link = "http://suninjuly.github.io/math.html"

# Driver initiation
driver = webdriver.Chrome()


# Function for calculating
def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))


try:
    # Open tested site link
    driver.get(link)

    # Find number in question
    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    calculated_Value = calc(x)

    # Input calculated value
    value_input = driver.find_element_by_id("answer")
    value_input.send_keys(calculated_Value)

    # Click on "I'm the robot" checkbox
    robot_checkbox = driver.find_element_by_css_selector('[for="robotCheckbox"]')
    robot_checkbox.click()

    # Click on "Robots rule" radiobutton
    robot_radio_button = driver.find_element_by_css_selector('[for="robotsRule"]')
    robot_radio_button.click()

    # Click on submit button
    submit_button = driver.find_element_by_class_name("btn.btn-default")
    submit_button.click()

finally:
    time.sleep(15)
    driver.quit()
