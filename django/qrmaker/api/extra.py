from rest_framework import serializers
from qrmaker.models import *


class FilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.exclude(state__in=["Deleted", "Archived"])
        return super(FilteredListSerializer, self).to_representation(data)


class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        list_serializer_class = FilteredListSerializer
        fields = ["uid", "state", "size", "date_added"]
