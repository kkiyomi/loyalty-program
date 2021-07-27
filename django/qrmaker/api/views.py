from qrmaker.models import Maker
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class MakerListAPIView(generics.ListAPIView):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer


class MakerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Maker.objects.all()
    serializer_class = MakerDetailSerializer
    lookup_field = "uid"


class PromoCreateAPIView(generics.CreateAPIView):
    queryset = Promo.objects.all()
    serializer_class = PromoAddSerializer

    """
    {
        "title": "5",
        "description": "5",
        "size": 5,
        "maker": 2
    }
    """

    def create(self, request, *args, **kwargs):
        if not Maker.objects.filter(uid=self.kwargs["maker_uid"]).exists() or (
            Maker.objects.get(id=request.data["maker"]).uid != self.kwargs["maker_uid"]
        ):
            resp = {
                "msg": "Error",
            }
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
