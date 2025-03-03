from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class CartPage:

    def check_product(self, product_name):
        browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/textViewProductTitle')).should(have.text(product_name))
