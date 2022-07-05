from rest_framework import serializers
from .models import Product
from accounts.serializers import AccountSerializer

class ProductSerializer(serializers.ModelSerializer):
    seller = AccountSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "description",
            "price",
            "quantity",
            "is_active",
            "seller_id"
        ]