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
        fields = [
            "title",
            "description",
            "uid",
            "suid",
            "target",
            "state",
            "size",
            "date_added",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["pi_count"] = PromoInstance.objects.filter(
            promo=instance
        ).count()

        progress = (representation["pi_count"] / instance.target) * 100
        representation["progress"] = f"{progress}%"

        return representation


class MakerDetailSerializer(serializers.ModelSerializer):
    promos = _PromoListSerializer(many=True, read_only=True)

    class Meta:
        model = Maker
        fields = ["username", "title", "description", "uid", "date_added", "promos"]
        read_only_fields = ["date_added", "promos", "uid"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["pr_count"] = instance.promos.exclude(
            state__in=["Deleted", "Archived"]
        ).count()
        representation["pi_count"] = (
            PromoInstance.objects.filter(promo__maker=instance)
            .exclude(promo__state__in=["Deleted", "Archived"])
            .count()
        )
        representation["ts_count"] = (
            Transaction.objects.filter(pinstance__promo__maker=instance)
            .exclude(pinstance__promo__state__in=["Deleted", "Archived"])
            .count()
        )

        return representation
