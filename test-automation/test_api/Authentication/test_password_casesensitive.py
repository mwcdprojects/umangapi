import requests
from src import *
from src.Access import *
from cryptography.fernet import Fernet
import json


class test_userauthentication:

    def __init__(self):
        self.loginid = credentials.ffdeo_user['ffdeouserlogin']
        self.password = credentials.ffdeo_user['encryptedpassword']
        self.url = URLs.userauthenticationurl

    def test_login_password_partial_uppercase(self):
        print("Access User Authenticationapi")
        print("Passing password with few Uppercase characters")
        self.password = self.password[:3].upper() + self.password[3:]
        endpoint = self.url
        payload = {"Username": self.loginid, "Password": self.password}
        print("Payload: {}".format(payload))
        response = requests.post(endpoint, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'failure'
        assert response.json()['errormessage'] == 'somthing went wrong'

    def test_login_password_uppercase(self):
        print("Access User Authenticationapi")
        print("Passing password with full uppercase characters.")
        self.password = self.password.upper()
        endpoint = self.url.format(self.loginid, self.password)
        endpoint = self.url
        payload = {"Username": self.loginid, "Password": self.password}
        print ("Payload: {}".format(payload))
        response = requests.post(endpoint, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'failure'
        assert response.json()['errormessage'] == 'somthing went wrong'


if __name__ == '__main__':
    test_userauthentication().test_login_password_partial_uppercase()
    test_userauthentication().test_login_password_uppercase()
