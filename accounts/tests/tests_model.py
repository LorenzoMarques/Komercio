from django.test import TestCase
from accounts.models import User
from products.models import Product
from django.db.utils import IntegrityError

# Create your tests here.

class AccountTest(TestCase):
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


    @classmethod
    def setUp(cls) -> None:
        print("Executando setUp")

    def test_user_fields(self):
        print("Executando test_seller_fields")
        self.assertEqual(self.user.email, self.email)
        self.assertEqual(self.user.password, self.password)
        self.assertEqual(self.user.first_name, self.first_name)
        self.assertEqual(self.user.last_name, self.last_name)
        self.assertEqual(self.user.is_seller, self.is_seller)
