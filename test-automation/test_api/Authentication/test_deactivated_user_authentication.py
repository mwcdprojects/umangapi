import requests
from src import *
from src.Access import *
from src import encrypt_decrypt
import json


class test_deactivate_userauthentication:

    def __init__(self):
        self.loginid = credentials.ffdeo_user['deactivated_user']
        self.password = credentials.ffdeo_user['deactivated_pwd']
        self.url = URLs.userauthenticationurl

    def test_login_failure(self):
        print("Access User Authenticationapi for deactivated user")
        print("Passing valid password to validate failure")
        endpoint = self.url
        payload = {"Username": self.loginid, "Password": self.password}
        response = requests.post(endpoint, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'failure'
        assert response.json()['errormessage'] == 'somthing went wrong'


if __name__ == '__main__':
    test_deactivate_userauthentication().test_login_failure()
