from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import *
from qrmaker.models import *


class MakerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Maker.objects.all()
    serializer_class = MakerDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        token = self.request.META.get("HTTP_AUTHORIZATION").split(" ")[-1]
        obj = queryset.get(user=Token.objects.get(key=token).user.id)

        self.check_object_permissions(self.request, obj)
        return obj
