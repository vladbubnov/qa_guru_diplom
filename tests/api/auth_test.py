import requests

# URL для запроса к CAPTCHA-сервису
captcha_url = 'https://smartcaptcha.yandexcloud.net/check'

# Параметры запроса
params = {
    'host': 'www.vseinstrumenti.ru',
    'sitekey': 'ysc1_rjUUmGoOrHx72bK28Mq1c9oHoDcWlxgwaYxeQ9Tza075e4b6',
    'href': 'https://www.vseinstrumenti.ru/user/favorites/'
}

# Заголовки запроса
# headers = {
#     'accept': '*/*',
#     'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
#     'content-type': 'text/plain;charset=UTF-8',
#     'origin': 'https://smartcaptcha.yandexcloud.net',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
# }

# Данные запроса
data = {
    'rdata': '...'  # Здесь должны быть ваши данные
}

# Выполнение запроса
response = requests.post(captcha_url, params=params, )

# Проверка ответа
if response.status_code == 200:
    smart_captcha_response = response.json().get('smartCaptchaResponse')
    print('SmartCaptchaResponse:', smart_captcha_response)
else:
    print('Ошибка при запросе CAPTCHA:', response.status_code, response.text)

# URL для запроса к API
api_url = 'https://bff.vseinstrumenti.ru/api/v1/user/login/email'

# Заголовки запроса
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.vseinstrumenti.ru',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

# Данные запроса
data = {
    'email': 'tt8260639@gmail.com',
    'password': 'testov11',
    'isMobile': False,
    'smartCaptchaResponse': smart_captcha_response  # Используйте полученный ответ
}

def test_auth():
    # Выполнение запроса
    response = requests.post(api_url, headers=headers, json=data)

    # Проверка ответа
    if response.status_code == 200:
        print('Успешный вход:', response.json())
    else:
        print('Ошибка при входе:', response.status_code, response.text)

def test_add_to_cart():
    import requests

    # URL для добавления продукта в корзину
    url = 'https://bff.vseinstrumenti.ru/api/v1/cart/product/add'

    # Заголовки запроса
    # headers = {
    #     'accept': 'application/json, text/plain, */*',
    #     'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
    #     'content-type': 'application/json',
    #     'origin': 'https://www.vseinstrumenti.ru',
    #     'priority': 'u=1, i',
    #     'referer': 'https://www.vseinstrumenti.ru/category/kabelnye-organajzery-i-organizatory-19-4432/',
    #     'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"macOS"',
    #     'sec-fetch-dest': 'empty',
    #     'sec-fetch-mode': 'cors',
    #     'sec-fetch-site': 'same-site',
    #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    #     'x-locality-id': '93b3df57-4c89-44df-ac42-96f05e9cd3b9',
    #     'token': '',  # Замените на актуальный токен, если требуется
    # }

    # Cookies
    # cookies = {
    #     'spid': '1740118159025_1cf95358812f22095ea44f8a81a81864_d92j1koqc9s1lltg',
    #     'vi_represent_id': '116',
    #     'vi_represent_type': 'common',
    #     'wucf': '7',
    #     'vi_rr_id': '4ada6cd3-636a-4ba0-8a6e-2a71d9e1c7fc',
    #     'cartToken': '7b88b870-1bfc-41e3-af8f-6a0eb705b2f6',
    #     # Добавьте остальные cookies здесь...
    # }

    # Данные запроса
    data = {
        "productGuid": "ddb53b7e-ad49-474d-b85f-502cdc45de2c",
        "quantity": 1,
        "byPack": 0,
        "saleGuid": None
    }

    # Выполнение POST-запроса
    response = requests.post(url, json=data)

    # Проверка ответа
    if response.ok:
        print('Продукт успешно добавлен в корзину:', response.json())
    else:
        print('Ошибка при добавлении продукта:', response.status_code, response.text)