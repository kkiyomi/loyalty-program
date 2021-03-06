from rest_framework import serializers

from qrmaker.models import *


class _PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = ["title", "description", "size", "uid", "suid"]


class _TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["uid", "date_added"]


class PInstanceCreateSerializer(serializers.ModelSerializer):
    promo = _PromoSerializer(read_only=True)

    class Meta:
        model = PromoInstance
        fields = ["title", "description", "uid", "promo"]
        read_only_fields = ["uid", "promo"]

    def create(self, validated_data):
        promo_data = validated_data.copy()
        promo_data["promo"] = Promo.objects.get(
            suid=self.context["view"].kwargs.get("promo_suid")
        )
        return PromoInstance.objects.create(**promo_data)


class PInstanceRetrieveSerializer(serializers.ModelSerializer):
    promo = _PromoSerializer(read_only=True)
    transactions = _TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = PromoInstance
        fields = ["title", "description", "uid", "promo", "transactions"]
        read_only_fields = ["uid", "promo", "transactions"]


class PInstanceListSerializer(serializers.ModelSerializer):
    transactions = _TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = PromoInstance
        fields = ["title", "date_added", "uid", "transactions"]
        read_only_fields = ["uid", "transactions"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["ts_count"] = instance.transactions.count()

        return representation
