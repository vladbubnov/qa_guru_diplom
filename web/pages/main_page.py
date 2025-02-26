import time

import pytest
from selene import browser, by, query, have, be

from web.pages.cart_page import CartPage
from web.pages.favorites_page import FavoritesPage
from web.pages.modal_page import ModalPage


class MainPage:

    def open_page(self):
        browser.open("/")

    def open_search_product(self, product):
        browser.open(f"/search/?q={product}")

    def get_text_product_by_index(self, index):
        return browser.all('[data-test="product-title"]')[index].locate().text

    def check_count_product_cart(self, count_product):
        (browser.element('[data-test="cart-link"]').element('[class="badge-counter"]')
         .should(have.text(str(count_product))))

    def check_count_product_favorites(self, count_product):
        (browser.element('[data-test="favorite-icon"]')
         .element('[class="badge-counter"]').should(have.text(str(count_product))))

    def click_cart_button(self):
        browser.element('[data-test="cart-link"]').click()
        browser.element(by.text("Корзина")).should(be.visible)

    def click_favourites_button(self):
        browser.element('[data-test="favorite-icon"]').click()
        browser.element(by.text("Избранные товары")).should(be.visible)

    def add_product_by_index_to_cart(self, index):
        browser.all('[data-test="product-add-to-cart"]')[index].click()
        browser.element('[class="badge-counter"]').should(be.visible)

    def add_product_by_index_to_favorites(self, index):
        browser.all('[data-test="product-add-to-favorite"]')[index].click()
        browser.element('[class="badge-counter"]').should(be.visible)


@pytest.fixture(scope='function')
def add_product_to_cart(driver_management):
    main_page = MainPage()
    main_page.open_search_product("Саморез")
    driver_management.all('[data-test="product-add-to-cart"]').first.click()
    main_page.click_cart_button()

    yield CartPage


@pytest.fixture(scope='function')
def add_product_to_favorites(driver_management):
    main_page = MainPage()
    main_page.open_search_product("Саморез")
    driver_management.all('[data-test="product-add-to-favorite"]').first.click()
    driver_management.element('[class="badge-counter"]').should(be.visible)
    main_page.click_favourites_button()

    yield FavoritesPage
