import json

import allure
from requests import Response

from utils.Checking import Checking
from utils.api import Dummy_post_api

# Невозможность добавление поста, заполнив все поля в теле запроса невалидными данными.
@allure.description("Inability to add a post by filling in all fields in the request body with invalid data")
def test_inability_adding_post_by_filling_invalid_data():
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

# Невозможность добавления поста, установив в поле text строковое значение из 5-ти символов.
@allure.description("The inability to add a post by setting a string value of 5 characters in the text field.")
def test_inability_adding_post_by_setting_string_5_char_in_text_field():
    json_body = {
                    "text": "posts",
                    "image": "https://yandex.ru/images/search?pos=0&from=tabbar&"
                             "img_url=http%3A%2F%2Flikeni.ru"
                             "%2Fupload%2Fdelight.webpconverter%2Fupload%2Fmedialibrary%2F22f"
                             "%2FGoogle%2520ejfnelvyimrwxlifda.png.webp%3F163516820620468&text"
                             "=гугл+док&rpt=simage&lr=43",
                    "likes": 0,
                    "tags": ["tag1", "tag2"],
                    "owner": "60d0fe4f5311236168a109ca"
                }
    result_post: Response = Dummy_post_api.create_post(json_body)
    Checking.assert_status_code(result_post, 400)
    expected_keys = ["error", "data"]
    Checking.check_equal_json_keys(result_post, expected_keys)
    Checking.check_json_value(result_post, expected_keys[0], "BODY_NOT_VALID")
    Checking.check_json_value(result_post, expected_keys[1], {"text": "Path `text` (`5`) is shorter than the "
                                                                           "minimum allowed length (6)."})

# Невозможность добавления поста, установив в поле text строковое значение из 1001-го символа.
@allure.description("The inability to add a post by setting a string value of 1001 characters in the text field.")
def test_inability_adding_post_by_setting_string_1001_char_in_text_field():
    json_body = {
                    "text": "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                            "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                            "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                            "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                            "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                            "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                            "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                            "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                            "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                            "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                            "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                            "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypos",
                    "image": "https://yandex.ru/images/search?pos=0&from=tabbar&"
                             "img_url=http%3A%2F%2Flikeni.ru"
                             "%2Fupload%2Fdelight.webpconverter%2Fupload%2Fmedialibrary%2F22f"
                             "%2FGoogle%2520ejfnelvyimrwxlifda.png.webp%3F163516820620468&text"
                             "=гугл+док&rpt=simage&lr=43",
                    "likes": 0,
                    "tags": ["tag1", "tag2"],
                    "owner": "60d0fe4f5311236168a109ca"
                }
    result_post: Response = Dummy_post_api.create_post(json_body)
    Checking.assert_status_code(result_post, 400)
    expected_keys = ["error", "data"]
    Checking.check_equal_json_keys(result_post, expected_keys)
    Checking.check_json_value(result_post, expected_keys[0], "BODY_NOT_VALID")
    Checking.check_json_value(result_post, expected_keys[1], {"text": "Path `text` (`mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                                                                      "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                                                                      "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                                                                      "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                                                                      "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                                                                      "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                                                                      "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                                                                      "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                                                                      "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                                                                      "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                                                                      "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypost"
                                                                      "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypos"
                                                                      "`) is longer than the maximum allowed length (1000)."})

