from rest_framework import serializers

from qrmaker.models import *
from qrmaker.api.promo.serializers import *


class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["title", "description", "uid"]
        read_only_fields = ["uid"]

    def create(self, validated_data):
        transaction = validated_data.copy()
        transaction["pinstance"] = PromoInstance.objects.get(
            uid=self.context["view"].kwargs.get("pinstance_uid")
        )
        return Transaction.objects.create(**transaction)


class TransactionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["uid", "date_added"]
