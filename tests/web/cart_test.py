import allure

from conftest import browser_management
from web.pages.cart_page import CartPage
from web.pages.main_page import MainPage
from web.pages.main_page import add_product_to_cart


@allure.tag('web')
@allure.feature("Корзина")
class TestCart:

    @allure.story("Добавление/удаление из корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Vladislav Bubnov")
    @allure.description("Тест проверяет изменение счетчика товаров в корзине")
    def test_count_product_cart(self, browser_management):
        browser = browser_management
        main_page = MainPage()
        index = 1

        with allure.step("Открываем страницу шуроповертов"):
            browser.open("/category/akkumulyatornye-dreli-shurupoverty-15/")

        with allure.step("Добавляем товар в корзину"):
            main_page.add_product_by_index_to_cart(index)

        with allure.step("Добавляем счетчик товаров в корзине"):
            main_page.check_count_product_cart(index)

    @allure.story("Добавление/удаление из корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Vladislav Bubnov")
    @allure.description("Тест проверяет добавление товара в корзину")
    def test_add_product_to_cart(self, browser_management):
        browser = browser_management
        main_page = MainPage()
        cart_page = CartPage()
        index = 1

        with allure.step("Открываем страницу шуроповертов"):
            browser.open("/category/akkumulyatornye-dreli-shurupoverty-15/")

        with allure.step("Получаем наименование товара"):
            product_name = main_page.get_text_product_by_index(index)

        with allure.step("Добавляем товар в корзину"):
            main_page.add_product_by_index_to_cart(index)

        with allure.step("Переходим в корзину"):
            main_page.click_cart_button()

        with allure.step("Проверяем наличие добавленного товара в корзине"):
            cart_page.check_product(product_name)

    @allure.story("Добавление/удаление из корзины")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Vladislav Bubnov")
    @allure.description("Тест проверяет удаление товара из корзины")
    def test_remove_product_from_cart(self, add_product_to_cart):
        cart_page = CartPage()
        with allure.step("Добавляем товар в корзину"):
            add_product_to_cart()

        with allure.step("Удаляем товар из корзины"):
            cart_page.delete_product()

        with allure.step("Проверяем пустую корзину"):
            cart_page.check_empty_cart()
