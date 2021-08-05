from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import *


class AccountRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        token = self.request.META.get("HTTP_AUTHORIZATION").split(" ")[-1]
        obj = queryset.get(id=Token.objects.get(key=token).user.id)

        self.check_object_permissions(self.request, obj)
        return obj
