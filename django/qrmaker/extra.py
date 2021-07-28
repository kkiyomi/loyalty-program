from rest_framework import permissions
from rest_framework import serializers

from qrmaker.models import *


class MakerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        maker_uid = request.resolver_match.kwargs.get("maker_uid")
        promo_uid = request.resolver_match.kwargs.get("promo_uid")

        maker = Maker.objects.filter(uid=maker_uid).exists()
        promo = Promo.objects.filter(uid=promo_uid).exists()
        if request.method == "POST":
            return maker
        return maker and promo


class FilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.exclude(state__in=["Deleted", "Archived"])
        return super(FilteredListSerializer, self).to_representation(data)


class PromoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        list_serializer_class = FilteredListSerializer
        fields = ["uid", "state", "size", "date_added"]


class PromoActionChoices:
    def make_published(self, request, queryset):
        queryset.update(state="Published")

    def make_pending(self, request, queryset):
        queryset.update(state="Pending")

    def make_archive(self, request, queryset):
        queryset.update(state="Archived")

    def make_delete(self, request, queryset):
        queryset.update(state="Deleted")

    def make_complete(self, request, queryset):
        queryset.update(state="Completed")

    make_published.short_description = "Mark as Published"
    make_pending.short_description = "Mark as Pending"
    make_archive.short_description = "Mark as Archived"
    make_delete.short_description = "Mark as Deleted"
    make_complete.short_description = "Mark as Completed"