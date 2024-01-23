import os.path

import pytest
import requests

from api import Pets
from settings import VALID_EMAIL, VALID_PASSWORD

pt = Pets()


def test_get_token():
    status = pt.get_token[1]
    assert status == 200


def test_list_users():
    status = pt.get_list_users()[0]
    amount = pt.get_list_users()[1]
    assert status == 200
    assert amount


def test_post_pet():
    status = pt.post_pet()[1]
    pet_id = pt.post_pet()[0]
    assert status == 200
    assert pet_id


def test_get_pet_photo(pet_photo='tests\\photo\\cat.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status = pt.get_pet_photo()[0]
    assert status == 200


def test_get_pet_like():
    status = pt.get_pet_like()
    assert status == 403


def test_get_registered_delete():
    status = pt.get_registered_delete()
    assert status == 200


def test_get_pet_comment():
    status = pt.get_pet_like()
    assert status == 200


def test_post_pets_list():
    status = pt.post_pets_list()
    assert status == 200


def test_get_pet():
    status = pt.get_pet()[0]
    amount = pt.get_pet()[1]
    assert status == 200
    assert amount


def test_delete_pet():
    status = pt.delete_pet()
    assert status == 200
