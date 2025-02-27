import allure
import pytest
from allure_commons.types import Severity
from jsonschema import validate
from faker import Faker

from api.requests.pet_requests import create_new_pet, get_pet_by_id, delete_pet_by_id
from api.schemas.pet_schemas import create_pet, get_pet, delete_pet
from tests import conftest

faker = Faker("ru_RU")


@allure.tag('api')
@allure.feature('Питомцы')
@allure.link('https://petstore.swagger.io/', name='Petstore')
class TestPet:

    @allure.story('Создать питомца')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vladislav Bubnov')
    @conftest.api
    @pytest.mark.api
    def test_add_pet(self):
        pet_name = faker.user_name()
        response = create_new_pet(pet_name=pet_name)

        with allure.step('Проверяем статус код ответа'):
            assert response.status_code == 200

        with allure.step(f'Проверяем имя питомца {pet_name}'):
            assert response.json()['name'] == pet_name

        validate(response.json(), create_pet)

    @allure.story('Получить питомца')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vladislav Bubnov')
    @conftest.api
    @pytest.mark.api
    @pytest.mark.parametrize("pet_id, expected_status, expected_response", [
        (None, 200, faker.user_name()),
        (9999999999999, 404, "Pet not found")
    ])
    def test_get_pet(self, pet_id, expected_status, expected_response):

        if pet_id is None:
            pet = create_new_pet(pet_name=expected_response)
            response = get_pet_by_id(pet.json()['id'])
        else:
            response = get_pet_by_id(pet_id)

        with allure.step(f'Проверяем статус код ответа: {expected_status}'):
            assert response.status_code == expected_status

        if expected_status == 200:
            with allure.step(f'Проверяем имя питомца: {expected_response}'):
                assert response.json()['name'] == expected_response
            validate(response.json(), get_pet)
        elif expected_status == 404:
            with allure.step(f'Проверяем сообщение об ошибке: {expected_response}'):
                assert response.json()['message'] == expected_response

    @allure.story('Удалить питомца')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'Vladislav Bubnov')
    @conftest.api
    @pytest.mark.api
    @pytest.mark.parametrize("pet_id, expected_status, expected_message", [
        (None, 200, None),
        (999999, 404, None)
    ])
    def test_delete_pet(self, pet_id, expected_status, expected_message):
        if pet_id is None:
            pet_name = faker.user_name()
            pet = create_new_pet(pet_name=pet_name)
            pet_id = pet.json()['id']
            response = delete_pet_by_id(pet_id)
        else:
            response = delete_pet_by_id(pet_id)

        with allure.step('Проверяем статус код ответа'):
            assert response.status_code == expected_status

        if expected_status == 200:
            with allure.step(f'Проверяем id: {pet_id} удаленного питомца'):
                assert response.json()['message'] == str(pet_id)
                validate(response.json(), delete_pet)
