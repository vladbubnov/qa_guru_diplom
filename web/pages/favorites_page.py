from selene import browser, be, query, have, by


class FavoritesPage:

    def check_product(self, product_name):
        browser.element('[data-test="product-title"]').should(have.text(product_name))

    def delete_product(self):
        browser.element('[data-test="product-add-to-favorite"]').should(be.visible).click()

    def check_empty_favorites(self):
        browser.driver.refresh()
        browser.element(by.text("Список избранного пуст")).should(be.visible)
