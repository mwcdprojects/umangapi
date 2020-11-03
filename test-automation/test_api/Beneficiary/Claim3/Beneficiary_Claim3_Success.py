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


class test_Beneficiary_registration:
    def __init__(self):
        self.loginid = credentials.ffdeo_user['ffdeouserlogin_tr9']
        # self.password = credentials.ffdeo_user['encryptedpassword_tr9']
        self.password = encrypt_decrypt.encryptString(credentials.ffdeo_user['ffdeouserpassword_tr9'],
                                                      credentials.ffdeo_user['key']).decode('utf-8')
        self.accountno = ''.join(random.choice(string.digits) for i in range(18))
        self.url = URLs.beneficiary_claim_tr9


    def authtoken_userid(self):
        payload = {"Username": self.loginid, "Password": self.password}
        response = requests.post(URLs.userauthenticationurl_tr9, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        return response.json()


    def test_registration_claim3_success(self):
        print("Generate claim3 payload")
        with open(str(Path(__file__).parents[1]) + "\\payloads\\claim3.json")as f1:
            payload = json.loads(f1.read())
        authdata = test_Beneficiary_registration().authtoken_userid()
        payload['AuthToken'] = authdata['AuthToken']
        payload['UserId'] = authdata['UserId']
        endpoint = self.url
        print ("Accessing the endpoint: {}".format(self.url))
        response = requests.post(self.url, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'success'
        print ("Response: {}".format(response.json()))



if __name__ == '__main__':
    test_Beneficiary_registration().test_registration_claim3_success()
