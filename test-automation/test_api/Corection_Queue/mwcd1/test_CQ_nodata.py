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
class test_correction_q_nodata:
    def __init__(self):
        self.loginid = credentials.ffdeo_user['ffdeouserlogin']
        self.password = credentials.ffdeo_user['encryptedpassword']
        #self.password = encrypt_decrypt.encryptString(credentials.ffdeo_user['ffdeouserpassword_tr9'],credentials.ffdeo_user['key'])
        self.url = URLs.correction_queue

    def authtoken_userid(self):
        payload = {"Username": self.loginid, "Password": self.password}
        response = requests.post(URLs.userauthenticationurl, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        return response.json()

    def test_cq_nodata(self):
        print("Generate correction queue payload")
        with open(str(Path(__file__).parents[1])+"\\mwcd1\\correctionq.json")as f1:
            payload = json.loads(f1.read())
        authdata = test_correction_q_nodata().authtoken_userid()
        payload['LoginAuthToken'] = authdata['AuthToken']
        payload['UserId'] = authdata['UserId']
        payload['BeneficiaryId']=4029389
        endpoint = self.url
        response = requests.post(self.url, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'failure'
        assert response.json()['ErrMsg'] == "No data Foung against this beneficiary"

if __name__ == '__main__':
    test_correction_q_nodata().test_cq_nodata()

