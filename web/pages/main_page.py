import pytest
from selene import browser, by, have, be

from web.pages.cart_page import CartPage
from web.pages.favorites_page import FavoritesPage


class MainPage:

    def open_page(self):
        browser.open("/")

    def open_product(self, product):
        browser.open(f"/product/{product}")

    def get_text_product(self):
        return browser.element('[data-test="product-title"]').locate().text

    def check_count_product_cart(self, count_product):
        (browser.element('[data-test="cart-link"]').element('[class="badge-counter"]')
         .should(have.text(str(count_product))))

    def check_count_product_favorites(self, count_product):
        (browser.element('[data-test="favorite-icon"]')
         .element('[class="badge-counter"]').should(have.text(str(count_product))))

    def click_cart_button(self):
        browser.element('[data-test="cart-link"]').should(be.visible).click()
        browser.element(by.text("Корзина")).should(be.visible)

    def click_favourites_button(self):
        browser.element('[data-test="favorite-icon"]').should(be.visible).click()
        browser.element(by.text("Избранные товары")).should(be.visible)

    def add_product_to_cart(self):
        browser.element('[data-test="add-to-cart-button"]').should(be.visible).click()

    def add_product_to_favorites(self):
        browser.element('[data-test="product-add-to-favorite-button"]').should(be.visible).click()


@pytest.fixture(scope='function')
def add_product_to_cart(driver_management):
    main_page = MainPage()
    main_page.open_product(126426)
    main_page.add_product_to_cart()
    main_page.click_cart_button()

    yield CartPage


@pytest.fixture(scope='function')
def add_product_to_favorites(driver_management):
    main_page = MainPage()
    main_page.open_product(126426)
    main_page.add_product_to_favorites()
    main_page.click_favourites_button()

    yield FavoritesPage
