from selenium_framework.pages.login_page import LoginPage
from selenium_framework.utilities.logger import Logger
import time

def test_valid_login(setup):
    logger = Logger.get_logger()
    driver = setup
    login = LoginPage(driver)

    logger.info("Opening Admin login page")
    login.open_url("https://admin-demo.nopcommerce.com/login")

    logger.info("Attempting login with valid credentials")
    login.login("admin@yourstore.com", "admin")

    time.sleep(2)

    logger.info("Verifying dashboard")
    assert "Dashboard" in driver.title

    logger.info("Login test passed")
