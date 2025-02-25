import allure

from tests.conftest import driver_management
from web.pages.favorites_page import FavoritesPage
from web.pages.main_page import MainPage, add_product_to_favorites


@allure.tag('web')
@allure.feature("Избранное")
@allure.story("Добавление/удаление из избранного")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Тест проверяет изменение счетчика товаров в избранном")
def test_count_product_cart(driver_management):
    browser = driver_management
    main_page = MainPage()
    index = 1

    with allure.step("Открываем страницу шуроповертов"):
        browser.open("/category/akkumulyatornye-dreli-shurupoverty-15/")

    with allure.step("Добавляем товар в избранное"):
        main_page.add_product_by_index_to_favorites(index)

    with allure.step("Добавляем счетчик товаров в избранном"):
        main_page.check_count_product_favorites(index)


@allure.tag('web')
@allure.feature("Избранное")
@allure.story("Добавление/удаление из избранного")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Тест проверяет добавление товара в избранное")
def test_add_product_to_favourites(driver_management):
    browser = driver_management
    main_page = MainPage()
    favorites_page = FavoritesPage()
    index = 1

    with allure.step("Открываем шуроповертов"):
        browser.open("/category/akkumulyatornye-dreli-shurupoverty-15/")

    with allure.step("Получаем наименование товара"):
        product_name = main_page.get_text_product_by_index(index)

    with allure.step("Добавляем товар в избранное"):
        main_page.add_product_by_index_to_favorites(index)

    with allure.step("Переходим в избранное"):
        main_page.click_favourites_button()

    with allure.step("Проверяем наличие добавленного товара в избранном"):
        favorites_page.check_product(product_name)


@allure.tag('web')
@allure.feature("Избранное")
@allure.story("Добавление/удаление из избранного")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Vladislav Bubnov")
@allure.description("Тест проверяет удаление товара из избранного")
def test_remove_product_from_cart(add_product_to_favorites):
    favorites_page = FavoritesPage()
    with allure.step("Добавляем товар в избранное"):
        add_product_to_favorites()

    with allure.step("Удаляем товар из корзины"):
        favorites_page.delete_product()

    with allure.step("Проверяем пустую корзину"):
        favorites_page.check_empty_favorites()
