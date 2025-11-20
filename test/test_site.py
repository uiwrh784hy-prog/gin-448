import time
from selenium.webdriver.common.by import By
from pages.homepage import Homepage
from pages.product import Productpage



def test_open_s6(browser):
    homepage = Homepage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = Productpage(browser)
    product_page.check_title_is('Samsung galaxy s6')



def test_two_monitors(browser):
    homepage = Homepage(browser)
    homepage.open()
    homepage.click_monitor()
    #monitor_link = browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    #monitor_link.click()
    time.sleep(3)
    homepage.check_products_count(2)
    #monitor = browser.find_elements(By.CSS_SELECTOR, '.card')
    #assert len(monitor) == 2


#def poe_ninja(browser):
    #browser.get('https://poe.ninja/')
    poe_economy_link = browser.find_element(By.CSS_SELECTOR, "a[href='/poe1/economy/keepers/currency']")
    poe_economy_link.click()
    div_cards = browser.find_element(By.XPATH, '''//span[text()='Divination Cards']''' )
    div_cards.click()
