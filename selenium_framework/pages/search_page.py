from selenium.webdriver.common.by import By
from selenium_framework.pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='button-1 search-box-button']")
    PRODUCT_TITLES = (By.XPATH, "//h2[@class='product-title']/a")

    def search(self, product):
        self.type(self.SEARCH_BOX, product)
        self.click(self.SEARCH_BUTTON)

    def results(self):
        return self.driver.find_elements(*self.PRODUCT_TITLES)
