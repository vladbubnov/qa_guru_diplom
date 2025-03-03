import allure
import pytest

from tests import conftest
from tests.conftest import driver_management
from pages.web.cart_page import CartPage
from pages.web.main_page import MainPage
from pages.web.main_page import add_product_to_cart

COUNT = 1
PRODUCT_ID = 126426


@allure.tag('web')
@allure.feature("Корзина")
class TestCart:

    @allure.story("Добавление/удаление из корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Vladislav Bubnov")
    @allure.description("Тест проверяет изменение счетчика товаров в корзине")
    @conftest.web
    @pytest.mark.web
    def test_count_product_cart(self, driver_management):
        main_page = MainPage()

        with allure.step(f"Открываем карточку товара id: {PRODUCT_ID}"):
            main_page.open_product(PRODUCT_ID)

        with allure.step("Добавляем товар в корзину"):
            main_page.add_product_to_cart()

        with allure.step(f"Проверяем значение {COUNT} счетчика товаров в корзине"):
            main_page.check_count_product_cart(COUNT)

    @allure.story("Добавление/удаление из корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Vladislav Bubnov")
    @allure.description("Тест проверяет добавление товара в корзину")
    @conftest.web
    @pytest.mark.web
    def test_add_product_to_cart(self, driver_management):
        main_page = MainPage()
        cart_page = CartPage()

        with allure.step(f"Открываем карточку товара id: {PRODUCT_ID}"):
            main_page.open_product(PRODUCT_ID)

        with allure.step("Получаем наименование товара"):
            product_name = main_page.get_text_product()

        with allure.step("Добавляем товар в корзину"):
            main_page.add_product_to_cart()

        with allure.step("Переходим в корзину"):
            main_page.click_cart_button()

        with allure.step("Проверяем наличие добавленного товара в корзине"):
            cart_page.check_product(product_name)

    @allure.story("Добавление/удаление из корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Vladislav Bubnov")
    @allure.description("Тест проверяет удаление товара из корзины")
    @conftest.web
    @pytest.mark.web
    def test_remove_product_from_cart(self, add_product_to_cart):
        cart_page = CartPage()
        with allure.step("Добавляем товар в корзину"):
            add_product_to_cart()

        with allure.step("Удаляем товар из корзины"):
            cart_page.delete_product()

        with allure.step("Проверяем пустую корзину"):
            cart_page.check_empty_cart()
