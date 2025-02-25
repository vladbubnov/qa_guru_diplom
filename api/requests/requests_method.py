import logging

import allure
import requests
from allure_commons.types import AttachmentType
from requests import Response


def post(url, headers, data):
    response = requests.post(
        url=url,
        headers=headers,
        data=data
    )
    logging_resp(response)
    logging_attach(response)
    return response


def get(url, params=None):
    response = requests.get(
        url=url,
        params=params
    )
    logging_resp(response)
    logging_attach(response)
    return response


def delete(url):
    response = requests.delete(
        url=url
    )
    logging_resp(response)
    logging_attach(response)
    return response


def logging_resp(response: Response):
    logging.info(f'With payload {response.request.body}')
    logging.info(f'Finished with status code {response.status_code}')


def logging_attach(response: Response):
    allure.attach(body=response.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
