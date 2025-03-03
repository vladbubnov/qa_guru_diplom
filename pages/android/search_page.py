from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class SearchPage:

    def open_product_card_by_index(self, index):
        browser.all((AppiumBy.ID, 'ru.handh.petrovich:id/textViewProductTitle'))[index].click()

    def add_product_to_cart_by_index(self, index):
        browser.all((AppiumBy.ID, 'ru.handh.petrovich:id/buttonProductAddToCart'))[index].click()

    def get_text_product_by_index(self, index):
        return browser.all((AppiumBy.ID, 'ru.handh.petrovich:id/textViewProductTitle'))[index].locate().text
