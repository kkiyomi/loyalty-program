from rest_framework import generics

from .serializers import *

from qrmaker.models import *
from qrmaker.extra import PInstancePermission


class PInstanceCreateAPIView(generics.CreateAPIView):
    queryset = PromoInstance.objects.all()
    serializer_class = PInstanceCreateSerializer
    permission_classes = [PInstancePermission]


class PInstanceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = PromoInstance.objects.all()
    serializer_class = PInstanceRetrieveSerializer
    lookup_field = "uid"
