import pytest
from appium import webdriver

@pytest.fixture()
def mobile_driver():
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Android",
        "appPackage": "com.android.calculator2",
        "appActivity": "com.android.calculator2.Calculator",
        "noReset": True
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()
