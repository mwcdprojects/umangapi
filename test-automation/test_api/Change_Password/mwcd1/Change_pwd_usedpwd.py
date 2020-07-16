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
class test_change_password:
    def __init__(self):
        self.url = URLs.change_pwd_mecd1



    def test_changepwd_usedpwd(self):
        print("Generate payload")
        payload = {}
        payload =  {"NewPassword":encrypt_decrypt.encryptString("Passw0rd123",credentials.ffdeo_user['key']).decode('utf-8')}
        payload['ConfirmPassword']=payload['NewPassword']


        endpoint = self.url
        response = requests.post(endpoint, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'failure'
        assert response.json()['errormessage'] == "This password was used before"

if __name__ == '__main__':
    test_change_password().test_changepwd_usedpwd()

