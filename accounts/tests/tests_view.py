from django.test import TestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from accounts.models import User

class TestView(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.seller = {
            "email":"teste@mail.com", 
            "password":"123456",
            "first_name": "teste", 
            "last_name":"etset",
            "is_seller":True
            }

        cls.consumer = {
            "email":"teste2@mail.com", 
            "password":"123456",
            "first_name": "teste2", 
            "last_name":"2etset",
            "is_seller":False
            }

    def test_register_seller_success(self):
        res = self.client.post("/api/accounts/", data=self.seller)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertNotIn("password", res.data)
        self.assertIn("email", res.data)
        self.assertIn("first_name", res.data)
        self.assertIn("last_name", res.data)
        self.assertEqual(res.data["is_seller"], True)

    def test_register_consumer_success(self):
        res = self.client.post("/api/accounts/", data=self.consumer)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertNotIn("password", res.data)
        self.assertIn("email", res.data)
        self.assertIn("first_name", res.data)
        self.assertIn("last_name", res.data)
        self.assertEqual(res.data["is_seller"], False)

    def test_register_failed(self):
        res = self.client.post("/api/accounts/", data={})

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", res.data)
        self.assertIn("email", res.data)
        self.assertIn("first_name", res.data)
        self.assertIn("last_name", res.data)

    def test_login_seller_success(self):
        self.client.post("/api/accounts/", data=self.seller)

        res = self.client.post("/api/login/", data={"email":self.seller["email"], "password":self.seller["password"]})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        self.assertIn("token", res.data)

    def test_login_consumer_success(self):
        self.client.post("/api/accounts/", data=self.consumer)

        res = self.client.post("/api/login/", data={"email":self.consumer["email"], "password":self.consumer["password"]})
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        self.assertIn("token", res.data)

    def test_list_users(self):

        response = self.client.get("/api/accounts/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)