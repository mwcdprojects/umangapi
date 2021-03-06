import requests
from src import *
import random
import logging
from src.Access import *
import string
from src import encrypt_decrypt
import json
from src.verhoeff import VerhoeffChecksum
from pathlib import Path
class test_forgot_password:
    def __init__(self):
        self.url = URLs.forget_pwd_mwcd1



    def test_forgot_pwd_invalid(self):
        print("Generate payload")
        payload =  {"UserName":"testautomation@example.com"}


        endpoint = self.url
        response = requests.post(endpoint, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'failure'
        assert response.json()['message'] == "Invalid Email"

if __name__ == '__main__':
    test_forgot_password().test_forgot_pwd_invalid()

