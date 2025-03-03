import allure
import pytest

from pages.android.cart_page import CartPage
from pages.android.main_page import MainPage
from pages.android.product_page import ProductPage
from pages.android.search_page import SearchPage
from tests import conftest

INDEX = 1
PRODUCT_NAME = "Саморез"


@allure.tag('android')
@allure.feature("Корзина")
class TestCart:

    @allure.story("Добавление в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Vladislav Bubnov")
    @allure.description("Тест проверяет добавление товара в корзину")
    @conftest.android
    @pytest.mark.android
    def test_add_product_to_cart(self, driver_management):
        main_page = MainPage()
        search_page = SearchPage()
        product_page = ProductPage()
        cart_page = CartPage()

        with allure.step("Пропускаем онбординг"):
            main_page.skip_onboarding()

        with allure.step(f"Выполняем поиск товара по наименованию: {PRODUCT_NAME}"):
            main_page.search_product(PRODUCT_NAME)

        # with allure.step(f"Откраем карточку товара по индексу: {INDEX}"):
        #     search_page.open_product_card_by_index(INDEX)

        with allure.step("Добавляем товар в корзину"):
            search_page.add_product_to_cart_by_index(INDEX)
            product_name = search_page.get_text_product_by_index(INDEX)

        with allure.step("Переходим в корзину"):
            main_page.click_cart_button()

        with allure.step("Проверяем наличие добавленного товара в корзине"):
            cart_page.check_product(product_name)
