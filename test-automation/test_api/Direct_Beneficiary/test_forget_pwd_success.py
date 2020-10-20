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
        self.url = URLs.direct_user_forgot_pwd



    def test_forgot_pwd_success(self):
        print("Generate payload")
        payload =  {"UserName":credentials.direct_ben_user['direct_ben_forgot_pwd_user']}


        endpoint = self.url
        response = requests.post(endpoint, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'success'
        assert response.json()['message'] == "Password reset link email has been sent to your email address"

if __name__ == '__main__':
    test_forgot_password().test_forgot_pwd_success()

