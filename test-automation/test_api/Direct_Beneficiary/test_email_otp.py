import requests
from src import *
from src.Access import *
from src import encrypt_decrypt
import json
class test_emailotp:

    def __init__(self):
        self.email = credentials.direct_ben_user['direct_ben_forgot_pwd_user']
        self.url = URLs.direct_ben_email_otp



    def test_otp_success(self):
        print("Access emailotp api")
        endpoint = self.url
        payload = {"email": self.email}
        response = requests.post(endpoint, data=json.dumps(payload),verify=False)
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'success'


if __name__ == '__main__':

    test_emailotp().test_otp_success()
