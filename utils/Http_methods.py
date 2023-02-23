import allure
import requests

from utils.logger_method import Logger


class Http_methods():
    headers = {"Content-Type": "application/json",
               "app-id": "63d7c78d900ded35d71002e3"
               }
    cookies = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookies)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
            Logger.add_response(result)
            return result


    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.get(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")
            result = requests.get(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookies)
            Logger.add_response(result)
            return result