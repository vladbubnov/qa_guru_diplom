import os
from typing import Literal

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from selenium.webdriver.chrome.options import Options

from utils import file

BASE_DIR = os.path.dirname(__file__)


class Config(BaseSettings):
    selenoid_login: str = ''
    selenoid_password: str = ''
    browser_version: str = ''
    base_url: str = 'https://www.vseinstrumenti.ru'
    context: Literal['local_emulator', 'bstack', 'web', 'api'] = 'web'
    driver_remote_url: str = ''
    bstack_userName: str = ''
    bstack_accessKey: str = ''
    timeout: float = 10.0
    # android_app_url: str = ''
    # appWaitActivity: str = ''
    #
    # android_platformVersion: Literal['11.0', '12.0', '13.0', '10.0'] = '11.0'
    # android_deviceName: str = ''
    # android_device_uid: str = ''
    # android_avd: str = ''

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

    def is_bstack_run(self):
        self.android_app_url.startswith('bs://')

    def driver_options(self, platform_name):
        if platform_name == 'android':
            options = UiAutomator2Options()

            if self.context == 'local_emulator':
                options.set_capability('remote_url', os.getenv('REMOTE_URL'))
                options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
                options.set_capability('appWaitActivity', os.getenv(
                    'APP_WAIT_ACTIVITY'))
                options.set_capability('app', file.relative_from_root(os.getenv('APP')))

            if self.context == 'bstack':
                options.set_capability('remote_url', os.getenv('REMOTE_URL'))
                options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
                options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
                options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
                options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
                options.set_capability('app', os.getenv('APP'))
                load_dotenv(dotenv_path=file.relative_from_root(
                    '.env.credentials'))
                options.set_capability(
                    'bstack:options', {
                        'projectName': '',
                        'buildName': 'browserstack-build-1',
                        'sessionName': 'BStack test',
                        'userName': os.getenv('USER_NAME'),
                        'accessKey': os.getenv('ACCESS_KEY'),
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
