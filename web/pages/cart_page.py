from selene import browser, have, by, be


class CartPage:

    def check_product(self, product_name):
        browser.element('[data-test="product-title"]').should(have.text(product_name))

    def delete_product(self):
        browser.element('[data-test="data-test-deleteCallback"]').click()

    def check_empty_cart(self):
        browser.element(by.text('Корзина пуста.')).should(be.visible)

