from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    CART_ICON = (By.CSS_SELECTOR, "a.ico-cart")
    CART_ITEM_ROWS = (By.CSS_SELECTOR, "table.cart tbody tr")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_cart(self):
        # Click on Shopping Cart icon
        cart_btn = self.wait.until(EC.element_to_be_clickable(self.CART_ICON))
        cart_btn.click()

    def cart_items_count(self):
        # Count number of rows inside the cart table
        try:
            items = self.wait.until(
                EC.presence_of_all_elements_located(self.CART_ITEM_ROWS)
            )
            return len(items)
        except:
            return 0
