import pytest
from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options

@pytest.fixture(scope="module")
def mobile_driver():

    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "emulator-5554",
        "appPackage": "com.google.android.dialer",
        "appActivity": "com.google.android.dialer.extensions.GoogleDialtactsActivity",
        "noReset": True
    })

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    yield driver
    driver.quit()
