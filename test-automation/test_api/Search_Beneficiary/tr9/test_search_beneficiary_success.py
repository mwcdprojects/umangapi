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
class test_search_beneficiary:
    def __init__(self):
        self.url = URLs.search_beneficiary_tr9



    def test_search_ben(self):
        print("Generate search beneficiary payload")
        with open(str(Path(__file__).parents[1])+"\\tr9\\search_ben.json")as f1:
            payload = json.loads(f1.read())


        endpoint = self.url
        response = requests.post(endpoint, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'success'

if __name__ == '__main__':
    test_search_beneficiary().test_search_ben()

