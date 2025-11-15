from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderConfirmationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def wait_for_thankyou_page(self):
        # Wait for URL to contain /checkout/completed
        return self.wait.until(EC.url_contains("/checkout/completed"))
