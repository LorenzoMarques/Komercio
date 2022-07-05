from rest_framework import generics
from .models import User
from .serializers import AccountSerializer, LoginSerializer, DeactivateSerializer
from rest_framework.views import APIView, Response, status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerPermission, IsSuperUserPermission

class AccountView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})

        return Response(
            {"detail": "invalid email or password"}, status.HTTP_401_UNAUTHORIZED
        )

class NewestView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        num = self.kwargs["num"]
        
        users = self.queryset.order_by("-date_joined")[0:num]

        return users

class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerPermission]

class AccountManagementView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = DeactivateSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUserPermission]