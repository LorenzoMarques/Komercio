from django.urls import path
from .views import ListCreateProductView, RetrieveUpdateProductView

urlpatterns = [
    path("products/", ListCreateProductView.as_view()),
    path("products/<pk>/", RetrieveUpdateProductView.as_view())
]