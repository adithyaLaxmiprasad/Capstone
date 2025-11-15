from selenium.webdriver.common.by import By
from selenium_framework.pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def login(self, email, password):
        email_input = self.driver.find_element(*self.EMAIL)
        password_input = self.driver.find_element(*self.PASSWORD)

        email_input.clear()
        password_input.clear()

        email_input.send_keys(email)
        password_input.send_keys(password)

        self.click(self.LOGIN_BUTTON)
