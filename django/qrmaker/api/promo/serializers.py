from rest_framework import serializers

from qrmaker.models import *


class _InstanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoInstance
        fields = ["title", "uid", "date_added"]


class PromoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = ["title", "description", "size", "uid", "suid"]
        read_only_fields = ["uid", "suid"]

    def create(self, validated_data):
        promo_data = validated_data.copy()
        promo_data["maker"] = Maker.objects.get(
            uid=self.context["view"].kwargs.get("maker_uid")
        )
        return Promo.objects.create(**promo_data)


class PromoRUDSerializer(serializers.ModelSerializer):
    pinstances = _InstanceListSerializer(many=True, read_only=True)

    class Meta:
        model = Promo
        fields = ["title", "description", "size", "state", "uid", "suid", "pinstances"]
        read_only_fields = ["uid", "suid", "pinstances"]

    def to_internal_value(self, data):
        for key in data.keys():
            if data[key] == "":
                data[key] = "N/A"
        return super().to_internal_value(data)
