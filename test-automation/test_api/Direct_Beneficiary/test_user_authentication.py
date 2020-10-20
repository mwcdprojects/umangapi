import requests
from src import *
from src.Access import *
from src import encrypt_decrypt
import json
class test_userauthentication:

    def __init__(self):
        self.loginid = credentials.direct_ben_user['direct_ben_user_tr9']
        self.password = credentials.direct_ben_user['direct_ben_pwd_tr9']
        self.pwd = encrypt_decrypt.encryptString(credentials.direct_ben_user['direct_ben_pwd_tr9'],credentials.ffdeo_user['key']).decode('utf-8')

        self.url = URLs.direct_user_auth



    def test_login_success(self):
        print("Access User Authenticationapi")
        print("Passing Valid credentials to validate successful login")
        endpoint = self.url
        payload = {"Username": self.loginid, "Password": self.pwd}
        response = requests.post(endpoint, data=json.dumps(payload),verify=False)
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'success'


if __name__ == '__main__':

    test_userauthentication().test_login_success()
