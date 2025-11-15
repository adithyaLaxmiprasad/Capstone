from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    FIRST_PRODUCT = (By.CSS_SELECTOR, "h2.product-title a")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_first_product(self):
        first = self.wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT))
        first.click()
