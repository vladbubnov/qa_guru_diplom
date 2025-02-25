import json

import allure

from api.requests.requests_method import post, get, delete

API_URL = 'https://petstore.swagger.io'
ENDPOINT_POST_PET = '/v2/pet/'


def create_new_pet(pet_name):
    payload = json.dumps({
        "name": pet_name
    })

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    full_url = API_URL + ENDPOINT_POST_PET

    with allure.step('Отправляем запрос на создание нового питомца'):
        return post(full_url, headers, payload)


def get_pet_by_id(pet_id):
    full_url = API_URL + ENDPOINT_POST_PET + f'{pet_id}'

    with allure.step('Отправляем запрос на получение питомца по id'):
        return get(full_url)


def delete_pet_by_id(pet_id):
    full_url = API_URL + ENDPOINT_POST_PET + f'{pet_id}'
    with allure.step('Отправляем запрос на удаления питомца по id'):
        return delete(full_url)
