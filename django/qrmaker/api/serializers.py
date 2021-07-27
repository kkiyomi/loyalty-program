from rest_framework import serializers
from qrmaker.models import *
from .extra import PromoSerializer


class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = ["id", "username", "uid", "date_added"]


class MakerDetailSerializer(serializers.ModelSerializer):
    promos = PromoSerializer(many=True, read_only=True)

    class Meta:
        model = Maker
        fields = ["username", "uid", "date_added", "promos"]


class PromoAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = ["title", "description", "size", "maker"]
