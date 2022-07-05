from django.urls import path

from .views import AccountView, LoginView, NewestView, AccountRetrieveUpdateDestroyAPIView, AccountManagementView

urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("login/", LoginView.as_view()),
    path("accounts/newest/<int:num>/", NewestView.as_view()),
    path("accounts/<pk>/", AccountRetrieveUpdateDestroyAPIView.as_view()),
    path("accounts/<pk>/management/", AccountManagementView.as_view())

]