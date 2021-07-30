from rest_framework import serializers

from qrmaker.models import *


class _FilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.exclude(state__in=["Deleted", "Archived"])
        return super(_FilteredListSerializer, self).to_representation(data)


class _PromoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        list_serializer_class = _FilteredListSerializer
        fields = ["uid", "suid", "state", "size", "date_added"]


class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = ["id", "username", "uid", "date_added"]


class MakerDetailSerializer(serializers.ModelSerializer):
    promos = _PromoListSerializer(many=True, read_only=True)

    class Meta:
        model = Maker
        fields = ["username", "title", "description", "uid", "date_added", "promos"]
        read_only_fields = ["date_added", "promos", "uid"]
