import json
import requests
import uuid

from requests_toolbelt.multipart.encoder import MultipartEncoder


class Pets:
    """ API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_registered_delete(self) -> json:
        """Запрос к Swagger для регистрации и удаления нового пользователя"""
        e = uuid.uuid4().hex
        data = {"email": f'lisa@{e}.ru',
                "password": 'cat1', "confirm_password": 'cat1'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_id = res.json().get('id')
        my_token = res.json()['token']
        headers = {'Authorization': f'Bearer {my_token}'}
        params = {'id': my_id}
        res = requests.delete(self.base_url + f'users/{my_id}', headers=headers, params=params)
        status = res.status_code
        return status

    def get_token(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
        data = {"email": 'lisaal@gmail.com',
                "password": 'never888'}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    def get_list_users(self):
        """Запрос к Swagger сайта для получения уникального id пользователя по токену"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json
        return status, amount

    def post_pet(self):
        """Запрос на создание питомца"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": 'Kisya', "type": 'cat', "age": 2, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def get_pet_photo(self):
        """Добавление фото питомца"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        files = {'pic': ('что угодно.jpg', open('tests\\photo\\cat.jpg', 'rb'), 'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        return status

    def get_pet_like(self):
        """Поставить лайк питомцу"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": 25711}
        res = requests.put(self.base_url + f'pet/{25711}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def get_pet_comment(self):
        """Оставить комментарий питомцу"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"pet_id": 25711, "message": 'nice pet!'}
        res = requests.put(self.base_url + f'pet/{25711}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def post_pets_list(self):
        """Запрос на вывод списка питомцев с указанными параметрами"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"type": 'dog', "pet_name": 'Max'}
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def get_pet(self):
        """Запрос к Swagger на получение информации о питомце по id"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/25711', headers=headers)
        status = res.status_code
        amount = res.json
        return status, amount

    def delete_pet(self) -> json:
        """Запрос на удаление питомца по id"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        params = {'id': 25712}
        res = requests.delete(self.base_url + f'pet/{25712}', headers=headers, params=params)
        status = res.status_code
        return status


Pets().get_registered_delete()
Pets().get_token()
Pets().get_list_users()
Pets().post_pet()
Pets().get_pet_photo()
Pets().get_pet_like()
Pets().get_pet_comment()
Pets().post_pets_list()
Pets().get_pet()
Pets().delete_pet()
