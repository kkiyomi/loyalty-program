from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import *


class RegistrationCreateAPIView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            account = Account.objects.get(email=serializer.data["email"])
            token = Token.objects.get(user=account.pk).key
            resp = {
                "data": serializer.data,
                "token": token,
                "msg": "Success",
            }
            return Response(resp, status=status.HTTP_201_CREATED)
        resp = {
            "data": serializer.errors,
            "msg": "Error",
        }
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)


class AccountRetrieveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        token = request.META.get("HTTP_AUTHORIZATION").split(" ")[-1]
        user = Account.objects.filter(id=Token.objects.get(key=token).user.id)
        serializer = AccountDetailSerializer(user, many=True)
        return Response(serializer.data)
