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
class test_correction_list_invalid_userid:
    def __init__(self):
        self.loginid = credentials.ffdeo_user['ffdeouserlogin']
        self.password = credentials.ffdeo_user['encryptedpassword']
        #self.password = encrypt_decrypt.encryptString(credentials.ffdeo_user['ffdeouserpassword_tr9'],credentials.ffdeo_user['key'])
        self.url = URLs.correction_list

    def authtoken_userid(self):
        payload = {"Username": self.loginid, "Password": self.password}
        response = requests.post(URLs.userauthenticationurl, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        return response.json()

    def test_cq_list_invalid_userid(self):
        print("Generate correction queue payload")
        with open(str(Path(__file__).parents[1])+"\\mwcd1\\correctionlist.json")as f1:
            payload = json.loads(f1.read())
        authdata = test_correction_list_invalid_userid().authtoken_userid()
        payload['LoginAuthToken'] = authdata['AuthToken']
        payload['UserId'] = authdata['UserId']
        payload['FF_DEOID'] = 12345
        endpoint = self.url
        response = requests.post(self.url, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'failure'
        assert response.json()['ErrMsg'] == 'Field Functionary Id is different from the one that the FF DEO user is tagged in'
        

if __name__ == '__main__':
    test_correction_list_invalid_userid().test_cq_list_invalid_userid()

