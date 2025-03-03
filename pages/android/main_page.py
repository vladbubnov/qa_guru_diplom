from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be


class MainPage:

    def search_product(self, product):
        (browser
         .element((AppiumBy.ID, 'ru.handh.petrovich:id/textInputEditTextSearch'))
         .click()
         .type(product)
         )
        browser.all((AppiumBy.ID, 'ru.handh.petrovich:id/textViewSuggestionValue')).first.click()

    def click_cart_button(self):
        browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/cart_graph')).click()

    def skip_onboarding(self):
        if browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/buttonAction')).should(be.visible):
            browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/buttonAction')).click()
            browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/buttonAction')).click()
            browser.element((AppiumBy.ID,
                            'com.android.permissioncontroller:id/permission_allow_foreground_only_button')).click()
            browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/statefulMaterialButtonSelectCity')).click()
            browser.element((AppiumBy.ID, 'ru.handh.petrovich:id/buttonAnotherTime')).click()




