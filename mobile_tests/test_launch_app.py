import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android.uiautomator2.base import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_youtube_search():

    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Android Emulator",
        "appPackage": "com.google.android.youtube",
        "appActivity": "com.google.android.youtube.HomeActivity",
        "noReset": True
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    time.sleep(5)

    # Click search button
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search").click()
    time.sleep(2)

    # Type song
    search_box = driver.find_element(AppiumBy.ID, "com.google.android.youtube:id/search_edit_text")
    search_box.send_keys("Karan Ahuja Forever Love")

    driver.press_keycode(66)  # ENTER
    time.sleep(3)

    # Click first video
    first_video = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.XPATH, "(//android.widget.ImageView)[1]"))
    )
    first_video.click()

    time.sleep(5)

    driver.quit()
