from selene import browser, be, query, have, by


class FavoritesPage:

    def check_product(self, product_name):
        browser.element('[class="main-container"]').element('[data-qa="products-tile"]').should(have.text(product_name))

    def delete_product(self):
        browser.element('[title="Удалить из избранного"]').click()
        browser.element(by.text('Товар удален из избранного')).should(be.visible)

    def check_empty_favorites(self):
        browser.driver.refresh()
        browser.element(by.text("В избранном пока нет товаров")).should(be.visible)
