from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
driver = webdriver.Chrome()


def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))


try:
    driver.get(link)
    treasure_icon = driver.find_element_by_id("treasure")
    treasure_value = treasure_icon.get_attribute('valuex')
    print(treasure_value)

    calculated_value = calc(treasure_value)
    text_input = driver.find_element_by_id('answer')
    text_input.send_keys(calculated_value)

    # Click on "I'm the robot" checkbox
    robot_checkbox = driver.find_element_by_id('robotCheckbox')
    robot_checkbox.click()

    # Click on "Robots rule" radiobutton
    robot_radio_button = driver.find_element_by_id('robotsRule')
    robot_radio_button.click()

    # Click on submit button
    submit_button = driver.find_element_by_css_selector('[type="submit"]')
    submit_button.click()


finally:
    time.sleep(7)
    driver.quit()

