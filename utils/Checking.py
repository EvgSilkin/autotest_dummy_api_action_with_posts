import json

import allure
from requests import Response

from utils.logger_method import Logger


class Checking:

    @staticmethod
    def assert_status_code(response: Response, status_code):
        assert response.status_code == status_code

    @staticmethod
    def check_equal_json_keys(response: Response, expected_keys):
        assert list(json.loads(response.text)) == expected_keys
    @staticmethod
    def check_json_value(response: Response, key_name, expected_value):
        dict_from_json = json.loads(response.text)
        fact_value = dict_from_json.get(key_name)
        assert fact_value == expected_value
    @staticmethod
    def check_each_json_value(response: Response, request_json):
        dict_from_json = json.loads(response.text)
        for key, value in request_json.items():
            if(key == "owner"):
                assert value == dict_from_json.get("owner").get("id")
            else:
                assert value == dict_from_json.get(key)


