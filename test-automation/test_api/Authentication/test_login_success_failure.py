import requests
from src import *
from src.Access import *
from src import encrypt_decrypt
import json
class test_userauthentication:

    def __init__(self):
        self.loginid = credentials.ffdeo_user['ffdeouserlogin_tr9']
        self.password = encrypt_decrypt.encryptString(credentials.ffdeo_user['ffdeouserpassword_tr9'],credentials.ffdeo_user['key']).decode('utf-8')
        self.url = URLs.userauthenticationurl_tr9

    def test_login_failure(self):
        print("Access User Authenticationapi")
        print("Passing incorrect password to validate failure")
        endpoint = self.url
        payload = {"Username":self.loginid,"Password":self.password+"abc"}
        response = requests.post(endpoint,data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'failure'
        assert response.json()['errormessage'] == 'somthing went wrong'

    def test_login_success(self):
        print("Access User Authenticationapi")
        print("Passing Valid credentials to validate successful login")
        endpoint = self.url
        payload = {"Username": self.loginid, "Password": self.password}
        response = requests.post(endpoint, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'success'


if __name__ == '__main__':
    test_userauthentication().test_login_failure()
    test_userauthentication().test_login_success()
