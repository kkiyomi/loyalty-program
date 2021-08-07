from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import *

from qrmaker.models import *
from qrmaker.extra import MakerPermission


class PromoCreateAPIView(generics.CreateAPIView):
    queryset = Promo.objects.all()
    serializer_class = PromoCreateSerializer
    permission_classes = [IsAuthenticated, MakerPermission]


class PromoUpdateDestroyAPIView(
    generics.UpdateAPIView,
    generics.DestroyAPIView,
):
    queryset = Promo.objects.all()
    serializer_class = PromoUpdateDestroySerializer
    permission_classes = [IsAuthenticated, MakerPermission]
    lookup_field = "uid"

    def perform_destroy(self, instance):
        instance.state = "Deleted"
        instance.save()
