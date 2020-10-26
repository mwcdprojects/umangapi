import requests
from src import *
from src.Access import *
from cryptography.fernet import Fernet
import json

class test_userauthentication:

    def __init__(self):
        self.loginid = credentials.ffdeo_user['ffdeouserlogin_tr9']
        self.password = encrypt_decrypt.encryptString(credentials.ffdeo_user['ffdeouserpassword_tr9'],
                                                      credentials.ffdeo_user['key']).decode('utf-8')
        self.url = URLs.userauthenticationurl_tr9

    def test_login_email_partial_uppercase(self):
        print("Access User Authenticationapi")
        print("Passing email partially uppercase")
        self.loginid = self.loginid[:3].upper()+self.loginid[3:]
        endpoint = self.url
        payload = {"Username": self.loginid, "Password": self.password}
        response = requests.post(endpoint, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'success'


    def test_login_email_uppercase(self):
        print("Access User Authenticationapi")
        print("Passing email with full uppercase characters")
        self.loginid = self.loginid.upper()
        endpoint = self.url
        payload = {"Username": self.loginid, "Password": self.password}
        response = requests.post(endpoint, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'success'



if __name__ == '__main__':
    test_userauthentication().test_login_email_partial_uppercase()
    test_userauthentication().test_login_email_uppercase()

