from selene import browser, be


class ModalPage:

    def click_close_button(self):
        browser.element('[class="modal-close"]').should(be.visible).click()