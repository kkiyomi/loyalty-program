from rest_framework import generics

from .serializers import *

from qrmaker.models import *
from qrmaker.extra import MakerPermission, PromoPermission


class PromoCreateAPIView(generics.CreateAPIView):
    queryset = Promo.objects.all()
    serializer_class = PromoCreateSerializer
    permission_classes = [MakerPermission]


class PromoRUDAPIView(
    generics.RetrieveAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView,
):
    queryset = Promo.objects.all()
    serializer_class = PromoRUDSerializer
    permission_classes = [MakerPermission, PromoPermission]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        obj = queryset.get(
            maker__uid=self.kwargs["maker_uid"],
            uid=self.kwargs["promo_uid"],
        )

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj