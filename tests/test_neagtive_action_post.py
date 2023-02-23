import json

import allure
from requests import Response

from utils.Checking import Checking
from utils.api import Dummy_post_api

# Добавление поста, заполнив все поля в теле запроса невалидными данными
@allure.description("Adding post by filling all fields in request body with invalid data")
def test_adding_post_by_filling_invalid_data():
    json_body = {
                    "text": 2023,
                    "image": 2023,
                    "likes": "test",
                    "tags": 2023,
                    "owner": 123
                }
    result_post: Response = Dummy_post_api.create_post(json_body)
    Checking.assert_status_code(result_post, 400)
    expected_keys = ["error", "data"]
    Checking.check_equal_json_keys(result_post, expected_keys)
    Checking.check_json_value(result_post, expected_keys[0], "BODY_NOT_VALID")
    Checking.check_json_value(result_post, expected_keys[1], {})