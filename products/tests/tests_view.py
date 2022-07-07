from django.test import TestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from accounts.models import User

class TestViewProduct(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.email = "teste@mail.com",
        cls.password = "123456",
        cls.first_name = "teste",
        cls.last_name = "etset",
        cls.is_seller = True

        cls.user = User.objects.create(
            email=cls.email, 
            password=cls.password, 
            first_name=cls.first_name,
            last_name=cls.last_name,
            is_seller=cls.is_seller
            )

    def test_list_products(self):

        response = self.client.get("/api/products/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)