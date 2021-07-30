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

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        obj = queryset.get(uid=self.kwargs["pinstance_uid"])

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj
