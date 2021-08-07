from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import *

from qrmaker.models import *
from qrmaker.extra import PInstancePermission, MakerPermission


class PInstanceCreateAPIView(generics.CreateAPIView):
    queryset = PromoInstance.objects.all()
    serializer_class = PInstanceCreateSerializer
    permission_classes = [PInstancePermission]


class PInstanceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = PromoInstance.objects.all()
    serializer_class = PInstanceRetrieveSerializer
    lookup_field = "uid"


class PInstanceListAPIView(generics.ListAPIView):
    queryset = PromoInstance.objects.all()
    serializer_class = PInstanceListSerializer
    permission_classes = [IsAuthenticated, MakerPermission]

    def get_queryset(self):
        promo_uid = self.kwargs["promo_uid"]
        queryset = PromoInstance.objects.filter(promo__uid=promo_uid)
        return queryset
