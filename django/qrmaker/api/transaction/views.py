from rest_framework import generics

from .serializers import *

from qrmaker.models import *


class TransactionCreateAPIView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionCreateSerializer


class TransactionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionRetrieveSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        obj = queryset.get(uid=self.kwargs["pinstance_uid"])

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj
