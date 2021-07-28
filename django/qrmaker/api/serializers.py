from rest_framework import serializers

from qrmaker.models import *
from qrmaker.extra import PromoListSerializer


class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = ["id", "username", "uid", "date_added"]


class MakerDetailSerializer(serializers.ModelSerializer):
    promos = PromoListSerializer(many=True, read_only=True)

    class Meta:
        model = Maker
        fields = ["username", "title", "description", "uid", "date_added", "promos"]
        read_only_fields = ["date_added", "promos", "uid"]


class PromoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = ["title", "description", "size", "uid"]
        read_only_fields = ["uid"]

    def create(self, validated_data):
        promo_data = validated_data.copy()
        promo_data["maker"] = Maker.objects.get(
            uid=self.context["view"].kwargs.get("maker_uid")
        )
        return Promo.objects.create(**promo_data)


class PromoRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = ["title", "description", "size", "uid"]
        read_only_fields = ["uid"]
