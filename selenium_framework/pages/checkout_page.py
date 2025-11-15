from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    LOGIN_EMAIL = (By.ID, "Email")
    LOGIN_PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.login-button")

    TERMS_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    BILLING_CONTINUE = (By.CSS_SELECTOR, "button.new-address-next-step-button")
    SHIPPING_METHOD_CONTINUE = (By.CSS_SELECTOR, "button.shipping-method-next-step-button")
    PAYMENT_METHOD_CONTINUE = (By.CSS_SELECTOR, "button.payment-method-next-step-button")
    PAYMENT_INFO_CONTINUE = (By.CSS_SELECTOR, "button.payment-info-next-step-button")
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, "button.confirm-order-next-step-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Step 1 — First Checkout attempt
    def begin_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.TERMS_CHECKBOX)).click()
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()

    # Step 2 — After Login, user is redirected back to cart again
    def login_checkout(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_EMAIL)).send_keys("testauto123@gmail.com")
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_PASSWORD)).send_keys("Test@12345")
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

        # MUST click terms again after redirection
        self.wait.until(EC.element_to_be_clickable(self.TERMS_CHECKBOX)).click()
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()

    # Step 3 — Finish Checkout Steps
    def complete_checkout_steps(self):
        self.wait.until(EC.element_to_be_clickable(self.BILLING_CONTINUE)).click()
        self.wait.until(EC.element_to_be_clickable(self.SHIPPING_METHOD_CONTINUE)).click()
        self.wait.until(EC.element_to_be_clickable(self.PAYMENT_METHOD_CONTINUE)).click()
        self.wait.until(EC.element_to_be_clickable(self.PAYMENT_INFO_CONTINUE)).click()
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_ORDER_BUTTON)).click()
