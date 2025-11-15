from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.button-1.add-to-cart-button")
    SUCCESS_BAR_TEXT = (By.CSS_SELECTOR, "div.bar-notification.success p")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_to_cart(self):
        add_btn = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN))
        add_btn.click()

        # Wait for success text to appear and confirm
        success_msg = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_BAR_TEXT)
        )
        print(f"Add to cart message: {success_msg.text}")

        # Wait until success popup disappears
        self.wait.until(EC.invisibility_of_element_located(self.SUCCESS_BAR_TEXT))
