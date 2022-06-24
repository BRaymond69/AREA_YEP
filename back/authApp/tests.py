from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationTest(APITestCase):
    
    def testRegistration(self):
        data = {"username": "testcase", "email": "test@local.app", "password": "strongpassword"} # <--- data to send for registration
        
        response = self.client.post("/register/", data)
        # print('\n\n' + str(response.json()) + '\n\n')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginTest(APITestCase):

    def testLogin(self):
        data = {"username": "testcase", "email": "test@local.app", "password": "strongpassword"}
        response = self.client.post("/register/", data)

        data = {"username": "testcase", "password": "strongpassword"} # <--- data to send for login
        response = self.client.post("/login/", data)
        # print('\n\n' + str(response.json()) + '\n\n')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
