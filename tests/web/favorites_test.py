import allure
import pytest

from tests import conftest
from tests.conftest import driver_management
from web.pages.favorites_page import FavoritesPage
from web.pages.main_page import MainPage, add_product_to_favorites

COUNT = 1
PRODUCT_ID = 126426


@allure.tag('web')
@allure.feature("Избранное")
class TestFavorites:

    @allure.story("Добавление/удаление из избранного")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Vladislav Bubnov")
    @allure.description("Тест проверяет изменение счетчика товаров в избранном")
    @conftest.web
    @pytest.mark.web
    def test_count_product_cart(self, driver_management):
        main_page = MainPage()

        with allure.step(f"Открываем карточку товара id: {PRODUCT_ID}"):
            main_page.open_product(PRODUCT_ID)

        with allure.step("Добавляем товар в избранное"):
            main_page.add_product_to_favorites()

        with allure.step("Добавляем счетчик товаров в избранном"):
            main_page.check_count_product_favorites(COUNT)

    @allure.story("Добавление/удаление из избранного")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Vladislav Bubnov")
    @allure.description("Тест проверяет добавление товара в избранное")
    @conftest.web
    @pytest.mark.web
    def test_add_product_to_favourites(self, driver_management):
        main_page = MainPage()
        favorites_page = FavoritesPage()

        with allure.step(f"Открываем карточку товара id: {PRODUCT_ID}"):
            main_page.open_product(PRODUCT_ID)

        with allure.step("Получаем наименование товара"):
            product_name = main_page.get_text_product()

        with allure.step("Добавляем товар в избранное"):
            main_page.add_product_to_favorites()

        with allure.step("Переходим в избранное"):
            main_page.click_favourites_button()

        with allure.step("Проверяем наличие добавленного товара в избранном"):
            favorites_page.check_product(product_name)

    @allure.story("Добавление/удаление из избранного")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Vladislav Bubnov")
    @allure.description("Тест проверяет удаление товара из избранного")
    @conftest.web
    @pytest.mark.web
    def test_remove_product_from_cart(self, add_product_to_favorites):
        favorites_page = FavoritesPage()
        with allure.step("Добавляем товар в избранное"):
            add_product_to_favorites()

        with allure.step("Удаляем товар из корзины"):
            favorites_page.delete_product()

        with allure.step("Проверяем пустую корзину"):
            favorites_page.check_empty_favorites()
