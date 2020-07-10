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
class test_Beneficiary_registration:
    def __init__(self):
        self.loginid = credentials.ffdeo_user['ffdeouserlogin']
        self.password = credentials.ffdeo_user['encryptedpassword']
        self.url = URLs.beneficiary_registration
        self.aacno = ''.join(random.choice('0123456789') for i in range(14))
        self.aadhaar1 = VerhoeffChecksum().generateVerhoeff(
            ''.join(random.choice(string.digits) for i in range(1, 12)))
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        for i in range(20):
            if int(self.aadhaar1[0]) == 0:
                self.aadhaar1 = VerhoeffChecksum().generateVerhoeff(
                    ''.join(random.choice(string.digits) for i in range(1, 12)))
            else:
                break
        self.aadhaar2 = VerhoeffChecksum().generateVerhoeff(
            ''.join(random.choice(string.digits) for i in range(1, 12)))
        for i in range(20):
            if int(self.aadhaar2[0]) == 0:
                self.aadhaar2 = VerhoeffChecksum().generateVerhoeff(
                    ''.join(random.choice(string.digits) for i in range(1, 12)))
            else:
                break

    def authtoken_userid(self):
        payload = {"Username": self.loginid, "Password": self.password}
        response = requests.post(URLs.userauthenticationurl, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        return response.json()

    def test_registration(self):
        print("Generate registration payload")
        with open(str(Path(__file__).parents[1])+"\\payloads\\Registration.json")as f1:
            payload = json.loads(f1.read())
        authdata = test_Beneficiary_registration().authtoken_userid()
        payload['AuthToken'] = authdata['AuthToken']
        payload['UserId'] = authdata['UserId']
        print ("Ben Aadhaarno: {}".format(self.aadhaar1))
        encrypted_aadhaar1 = encrypt_decrypt.encryptString(self.aadhaar1,credentials.ffdeo_user['aadhaarkey'])
        print ("Encrypted Ben Aadhaar no:{}".format(encrypted_aadhaar1))
        print("Husband Aadhaarno: {}".format(self.aadhaar2))
        encrypted_husband_aadhaarno = encrypt_decrypt.encryptString(self.aadhaar2,credentials.ffdeo_user['aadhaarkey'])
        print("Encrypted Husband Aadhaar no:{}".format(encrypted_husband_aadhaarno))
        payload['AadharNo'] = encrypted_aadhaar1.decode('utf-8')
        payload['HusbandAadhaarNo'] = encrypted_husband_aadhaarno.decode('utf-8')
        payload['BankAccountNo'] = self.aacno
        payload['BeneficiaryRegistrationDate'] = "2020-06-16"
        payload['DateOfMCPCard'] = "2020-01-01"
        print ("LMPDate: {}".format(payload['LMPDate']))
        print("BeneficiaryRegistrationDate: {}".format(payload['BeneficiaryRegistrationDate']))
        print("MCPDate: {}".format(payload['DateOfMCPCard']))
        endpoint = self.url
        response = requests.post(self.url, data=json.dumps(payload))
        print("Response: {}".format(response.json()))
        assert response.json()['status'] == 'success'

if __name__ == '__main__':
    test_Beneficiary_registration().test_registration()

