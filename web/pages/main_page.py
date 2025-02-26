import time

import pytest
from selene import browser, by, query, have, be

from web.pages.cart_page import CartPage
from web.pages.favorites_page import FavoritesPage
from web.pages.modal_page import ModalPage


class MainPage:

    def get_text_product_by_index(self, index):
        return browser.all('[data-qa="product-name"]')[index].get(query.attribute('title'))

    def check_count_product_cart(self, count_product):
        browser.element('[data-qa="cart-badge"]').should(have.text(str(count_product)))

    def check_count_product_favorites(self, count_product):
        browser.element('[data-qa="favorites-badge"]').should(have.text(str(count_product)))

    def click_cart_button(self):
        browser.element('[data-qa="cart"]').click()
        browser.element(by.text("Корзина")).should(be.visible)

    def click_favourites_button(self):
        browser.element('[data-qa="favorites"]').click()
        browser.element(by.text("Избранное")).should(be.visible)

    def add_product_by_index_to_cart(self, index):
        browser.all('[data-qa="product-add-to-cart-button"]')[index].click()
        browser.element('[data-qa="cart-badge"]').should(be.visible)
        ModalPage().click_close_button()

    def add_product_by_index_to_favorites(self, index):
        browser.all('[data-qa="product-vertical-toggle-favorites"]')[index].click()
        browser.element('[data-qa="favorites-badge"]').should(be.visible)


    def search_product(self, name):
        browser.element('[id="search-input"]').click()
        browser.element('[type="search"]').type(name).press_enter()

    def add_to_cart(self, index):
        browser.all('[class="favorite-label"]')[index].click()


@pytest.fixture(scope='function')
def add_product_to_cart(driver_management):
    driver_management.open("/category/akkumulyatornye-dreli-shurupoverty-15/")
    driver_management.all('[data-qa="product-add-to-cart-button"]').first.click()
    ModalPage().click_close_button()
    MainPage().click_cart_button()

    yield CartPage


@pytest.fixture(scope='function')
def add_product_to_favorites(driver_management):
    driver_management.open("/category/akkumulyatornye-dreli-shurupoverty-15/")
    driver_management.all('[data-qa="product-vertical-toggle-favorites"]').first.click()
    driver_management.element('[data-qa="favorites-badge"]').should(be.visible)
    MainPage().click_favourites_button()

    yield FavoritesPage
