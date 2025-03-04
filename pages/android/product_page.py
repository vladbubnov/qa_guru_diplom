from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class ProductPage:

    def add_product_to_cart(self):
        browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/textViewProductTitle')).click()

    def get_text_product(self):
        return browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/textViewTitle')).locate().text

