from rest_framework import generics

from .serializers import *
from qrmaker.models import *


class MakerListAPIView(generics.ListAPIView):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer


class MakerRetrieveAPIView(
    generics.RetrieveAPIView,
    generics.UpdateAPIView,
):
    queryset = Maker.objects.all()
    serializer_class = MakerDetailSerializer
    lookup_field = "uid"
