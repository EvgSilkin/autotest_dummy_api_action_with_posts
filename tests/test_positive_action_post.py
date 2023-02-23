import json

import allure
from requests import Response

from utils.Checking import Checking
from utils.api import Dummy_post_api

# Добавление поста, заполнив все поля в теле запроса валидными данными.
@allure.description("Adding post by filling all fields in request body with valid data")
def test_adding_post_by_filling_valid_data():
    json_body = {
                    "text": "New post from postman",
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
    Checking.assert_status_code(result_post, 200)
    expected_keys = ['id', 'image', 'likes', 'link', 'tags', 'text', 'publishDate', 'updatedDate', 'owner']
    Checking.check_equal_json_keys(result_post, expected_keys)
    Checking.check_json_value(result_post, "likes", 0)
    Checking.check_each_json_value(result_post, json_body)

# Добавление поста, установив в поле text строковое значение из 6-ти символов.
@allure.description("Adding a post by setting a string value of 6 characters in the text field")
def test_adding_post_by_setting_string_6_char_in_text_field():
    json_body = {
                    "text": "mypost",
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
    Checking.assert_status_code(result_post, 200)
    expected_keys = ['id', 'image', 'likes', 'link', 'tags', 'text', 'publishDate', 'updatedDate', 'owner']
    Checking.check_equal_json_keys(result_post, expected_keys)
    Checking.check_json_value(result_post, "likes", 0)
    Checking.check_each_json_value(result_post, json_body)

# Добавление поста, установив в поле text строковое значение из 1000-ти символов.
@allure.description("Adding a post by setting a string value of 1000 characters in the text field")
def test_adding_post_by_setting_string_1000_char_in_text_field():
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
                            "mypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypostmypo",
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
    Checking.assert_status_code(result_post, 200)
    expected_keys = ['id', 'image', 'likes', 'link', 'tags', 'text', 'publishDate', 'updatedDate', 'owner']
    Checking.check_equal_json_keys(result_post, expected_keys)
    Checking.check_json_value(result_post, "likes", 0)
    Checking.check_each_json_value(result_post, json_body)
