import requests
from src import *
from src.Access import *
from cryptography.fernet import Fernet


class test_userauthentication:

    def __init__(self):
        self.loginid = credentials.ffdeo_user['ffdeouserlogin']
        self.password = credentials.ffdeo_user['password']
        self.url = URLs.userauthenticationurl

    def test_login_failure(self):
        print("Access User Authenticationapi")
        print("Passing incorrect password to validate failure")
        endpoint = self.url.format(self.loginid, self.password) + "abc"
        resposne = requests.get(endpoint)
        print("Resposne: {}".format(resposne.json()))
        assert resposne.json()['status'] == 'failure'
        assert resposne.json()['errMsg'] == 'Email or Password not found'

    def test_login_success(self):
        print("Access User Authenticationapi")
        print("Passing Valid credentials to validate successful login")
        endpoint = self.url.format(self.loginid, self.password)
        resposne = requests.get(endpoint)
        print("Resposne: {}".format(resposne.json()))
        assert resposne.json()['status'] == 'success'


if __name__ == '__main__':
    test_userauthentication().test_login_failure()
    test_userauthentication().test_login_success()
