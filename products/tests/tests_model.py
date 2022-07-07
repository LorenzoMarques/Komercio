from django.test import TestCase
from accounts.models import User
from products.models import Product
from django.db.utils import IntegrityError

# Create your tests here.

class ProductTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.email = "teste@mail.com", 
        cls.password = "123456", 
        cls.first_name = "teste", 
        cls.last_name = "etset",
        cls.is_seller = True

        cls.seller = User.objects.create_user(
            email=cls.email[0], 
            password=cls.password[0], 
            first_name=cls.first_name[0],
            last_name=cls.last_name[0],
            is_seller=cls.is_seller
            )

        cls.description = "testProductDescription"
        cls.price = 100.99
        cls.quantity = 1

        cls.product = Product(
            description=cls.description,
            price=cls.price,
            quantity=cls.quantity
        )

    @classmethod
    def setUp(cls) -> None:
        print("Executando setUp")

    def test_create_product_withoud_user(self):
        print("Executando test_create_product_withoud_user")

        with self.assertRaises(IntegrityError):
            self.product.save()

    def test_create_product(self):
        print("Executando test_create_product")
        self.product.seller = self.seller
        self.product.save()

    def test_product_fields(self):
        print("Executando test_product_fields")
        self.product.seller = self.seller
        self.assertEqual(self.product.description, self.description)
        self.assertEqual(self.product.price, self.price)
        self.assertEqual(self.product.quantity, self.quantity)
        self.assertEqual(self.product.seller, self.seller)
        self.assertEqual(self.product.is_active, True)