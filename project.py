import os
from typing import Literal

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from selenium.webdriver.chrome.options import Options

from utils import file



class Config(BaseSettings):
    selenoid_login: str = ''
    selenoid_password: str = ''
    browser_version: str = ''
    base_url: str = 'https://petrovich.ru/'
    context: Literal['local_emulator', 'bstack', 'web', 'api'] = 'web'
    remote_url: str = ''
    bstack_userName: str = ''
    bstack_accessKey: str = ''
    timeout: float = 10.0
    platform_name: str = ''
    platform_version: str = ''
    android_app_url: str = ''
    app_wait_activity: str = ''
    app: str = ''
    device_name: str = ''

    @property
    def bstack_credentials(self):
        load_dotenv(file.relative_from_root('.env.bstack_credentials'))
        self.bstack_userName = os.getenv('bstack_userName')
        self.bstack_accessKey = os.getenv('bstack_accessKey')
        return {
            'userName': self.bstack_userName,
            'accessKey': self.bstack_accessKey
        }

    def get_selenoid_link(self):
        load_dotenv(file.relative_from_root('.env.selenoid_credentials'))
        self.selenoid_login = os.getenv('selenoid_login')
        self.selenoid_password = os.getenv('selenoid_password')
        return f"https://{self.selenoid_login}:{self.selenoid_password}@selenoid.autotests.cloud/wd/hub"

    def driver_options(self, platform_name):
        if platform_name == 'android':
            options = UiAutomator2Options()

            if self.context == 'local_emulator':
                load_dotenv(file.relative_from_root('.env.local_emulator'))
                options.set_capability('remote_url', os.getenv('REMOTE_URL'))
                options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
                options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
                options.set_capability('app', file.relative_from_root(os.getenv('APP')))

            if self.context == 'bstack':
                load_dotenv(file.relative_from_root('.env.bstack'))
                options.set_capability('remote_url', os.getenv('REMOTE_URL'))
                options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
                options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
                options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
                options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
                options.set_capability('app', os.getenv('APP'))
                options.set_capability(
                    'bstack:options', {
                        'projectName': 'petrovich',
                        'buildName': 'browserstack-petrovich',
                        'sessionName': 'BStack test',
                        **self.bstack_credentials
                    },
                )

            return options

        elif platform_name == 'web':
            options = Options()
            selenoid_capabilities = {
                "browserName": "chrome",
                "browserVersion": self.browser_version,
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True
                }
            }
            options.capabilities.update(selenoid_capabilities)

            return options
