from django.contrib.auth.models import AbstractUser
from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=127)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    seller = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="products")
