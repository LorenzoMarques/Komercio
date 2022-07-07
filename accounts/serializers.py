from rest_framework import serializers
from .models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_seller'
        ]
        extra_kwargs = {"password": {"write_only": True}}


    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("email already exists")

        return value

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        instance.email = validated_data.get("email", instance.email)
        password = validated_data.get("password")
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.is_seller = validated_data.get("is_seller", instance.is_seller)


        if password:
            instance.set_password(password)

        instance.save()

        return instance
        


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(write_only=True)

class DeactivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'is_active',
        ]