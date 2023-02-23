from utils.Http_methods import Http_methods

base_url = "https://dummyapi.io/data/v1/post"
key = ""
class Dummy_post_api():

    @staticmethod
    def create_post(json_post):
        url = base_url + "/create"
        result_post = Http_methods.post(url, json_post)
        return result_post
    @staticmethod
    def get_post(id):
        url = base_url + id
        result_get = Http_methods.get(url)
        return result_get
    @staticmethod
    def put_post(id, json_post):
        url = base_url + id
        result_put = Http_methods.put(url, json_post)
        return result_put
    @staticmethod
    def delete_post(id, json_post):
        url = base_url + id
        result_delete = Http_methods.delete(url, json_post)
        return result_delete