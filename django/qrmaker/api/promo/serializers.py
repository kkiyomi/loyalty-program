from rest_framework import serializers

from qrmaker.models import *


class _InstanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoInstance
        fields = ["title", "uid", "date_added"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["ts_count"] = Transaction.objects.filter(
            pinstance=instance
        ).count()

        return representation


class PromoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = ["title", "description", "size", "uid", "suid"]
        read_only_fields = ["uid", "suid"]

    def create(self, validated_data):
        promo_data = validated_data.copy()
        promo_data["maker"] = self.context["request"].user.maker
        return Promo.objects.create(**promo_data)


class PromoUpdateDestroySerializer(serializers.ModelSerializer):
    pinstances = _InstanceListSerializer(many=True, read_only=True)

    class Meta:
        model = Promo
        fields = [
            "title",
            "description",
            "size",
            "state",
            "uid",
            "suid",
            "date_added",
            "pinstances",
        ]
        read_only_fields = ["uid", "suid", "pinstances", "date_added"]

    def to_internal_value(self, data):
        for key in data.keys():
            if data[key] == "":
                data[key] = "N/A"
        return super().to_internal_value(data)
