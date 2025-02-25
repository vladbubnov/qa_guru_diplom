from selene import browser, have, by, be


class CartPage:

    def check_product(self, product_name):
        browser.element('[data-behavior="cart-product-name"]').should(have.text(product_name))

    def delete_product(self):
        browser.element('[data-behavior="cart-product-delete"]').click()
        browser.element(by.text('Товар удален из корзины')).should(be.visible)

    def check_empty_cart(self):
        browser.driver.refresh()
        browser.element('[data-behavior="cart-empty-title"]').should(be.visible)

