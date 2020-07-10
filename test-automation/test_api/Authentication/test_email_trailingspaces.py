import requests
from src import *
from src.Access import *
from cryptography.fernet import Fernet
import json

class test_userauthentication:

    def __init__(self):
        self.loginid = credentials.ffdeo_user['ffdeouserlogin']+"    "
        self.password = credentials.ffdeo_user['encryptedpassword']
        self.url = URLs.userauthenticationurl


    def test_login_email_trailingspaces(self):
        print("Access User Authenticationapi")
        print("Passing email with trailing spaces")
        endpoint = self.url
        payload = {"Username": self.loginid, "Password": self.password}
        print("Payload: {}".format(payload))
        response = requests.post(endpoint, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'failure'
        assert response.json()['errormessage'] == 'somthing went wrong'


if __name__ == '__main__':
    test_userauthentication().test_login_email_trailingspaces()

