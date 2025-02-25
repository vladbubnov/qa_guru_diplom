import os

import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser

# import config
from selenium.webdriver.chrome.options import Options

from utils import attach

DEFAULT_BROWSER_NAME = "chrome"
DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


# @pytest.fixture(scope='function')
# def mobile_management(context):
#     options = config.to_driver_options(context=context)
#
#     browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
#     browser.config.timeout = 10.0
#
#     yield
#
#     browser.quit()


@pytest.fixture(scope='function')
def browser_management(request):
    # browser_name = request.config.getoption('browser_name') or DEFAULT_BROWSER_NAME
    # browser_version = request.config.getoption('browser_version') or DEFAULT_BROWSER_VERSION
    #
    # options = Options()
    # selenoid_capabilities = {
    #     "browserName": browser_name,
    #     "browserVersion": browser_version,
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    # options.capabilities.update(selenoid_capabilities)
    #
    # selenoid_host = os.getenv("SELENOID_HOST")
    # selenoid_login = os.getenv("SELENOID_LOGIN")
    # selenoid_password = os.getenv("SELENOID_PASSWORD")
    #
    # driver = webdriver.Remote(
    #     command_executor=f"https://{selenoid_login}:{selenoid_password}@{selenoid_host}/wd/hub",
    #     options=options
    # )
    # browser.config.driver = driver

    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://www.vseinstrumenti.ru'

    yield browser

    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_html(browser)
    # attach.add_video(browser)

    browser.quit()
