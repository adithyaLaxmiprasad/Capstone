from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-box-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located(self.SEARCH_BOX))

    def search_product(self, keyword):
        box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BOX))
        box.clear()
        box.send_keys(keyword)
        btn = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        btn.click()
