from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.get('https://www.chrome.com')
search_input = driver.find_element_by_name('q')
search_input.send_keys('cat')
search_input.submit()
import