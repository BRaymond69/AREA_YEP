from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.

class ServiceTest(APITestCase):
    
    def testService(self):
        data = {"Authorization": "Token 63ff33fffdfb1eb3e97f4df96028ccf1c421119f"} # <--- data to send for registration
        
        response = self.client.post("/intra/", headers=data)
        # print('\n\n' + str(response.json()) + '\n\n')
        self.assertEqual(response.status_code, status.HTTP_200_OK)