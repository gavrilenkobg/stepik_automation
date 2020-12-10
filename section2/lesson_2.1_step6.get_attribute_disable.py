from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"
driver = webdriver.Chrome()

try:
    driver.get(link)
    people_radio = driver.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute('checked')
    assert people_checked == 'true', "People radio is not selected by default"

    robots_radio = driver.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

finally:
    time.sleep(15)
    driver.quit()

