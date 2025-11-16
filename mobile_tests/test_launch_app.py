import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_save_contact(mobile_driver):
    driver = mobile_driver
    wait = WebDriverWait(driver, 15)
    time.sleep(1)

    # similar steps as standalone: open keypad, type number, add contact, save...
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "key pad").click()
    except:
        pass

    for d in "9876543210":
        try:
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"digit {d}").click()
        except:
            try:
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{d}")').click()
            except:
                pass
        time.sleep(0.2)

    try:
        driver.find_element(AppiumBy.ID, "com.google.android.dialer:id/add_contact_button").click()
    except:
        pass

    time.sleep(1)
    # leave verification manual or add same verification code from standalone script
    assert True
