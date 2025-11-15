import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import allure
import os


def get_driver(browser):
    """Return WebDriver instance based on browser name."""

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Edge(options=options)

    else:
        raise ValueError("Unsupported browser! Use chrome or edge.")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to use: chrome or edge")


@pytest.fixture()
def setup(request):

    browser = request.config.getoption("--browser")
    driver = get_driver(browser)

    yield driver

    # Take screenshot on failure
    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"Failure - {request.node.name}",
            attachment_type=allure.attachment_type.PNG,
        )

    driver.quit()


# Hook for test result
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
