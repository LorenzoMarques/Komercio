from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ProductSerializer, ListProductSerializer
from .mixins import SerializerByMethodMixin
from .models import Product
from .permissions import ProductCustomPermission, IsOwnerPermission

# Create your views here.

class ListCreateProductView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, ProductCustomPermission]

    queryset = Product.objects.all()
    serializer_map = {
        "GET": ListProductSerializer,
        "POST": ProductSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class RetrieveUpdateProductView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerPermission]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
