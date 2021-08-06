from rest_framework import permissions
from rest_framework import serializers

from qrmaker.models import *


class MakerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        maker_uid = request.resolver_match.kwargs.get("maker_uid")
        maker = Maker.objects.filter(uid=maker_uid).exists()
        return maker


class PromoPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        promo_uid = request.resolver_match.kwargs.get("promo_uid")
        promo = Promo.objects.filter(uid=promo_uid).exists()
        return promo


class PInstancePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        promo_suid = request.resolver_match.kwargs.get("promo_suid")
        promo = Promo.objects.filter(suid=promo_suid).exists()
        return promo


class PromoActionChoices:
    def make_published(self, request, queryset):
        queryset.update(state="Published")

    def make_pending(self, request, queryset):
        queryset.update(state="Pending")

    def make_archive(self, request, queryset):
        queryset.update(state="Archived")

    def make_delete(self, request, queryset):
        queryset.update(state="Deleted")

    def make_completed(self, request, queryset):
        queryset.update(state="Completed")

    def make_complete(self, request, queryset):
        queryset.update(state="Completed")

    make_published.short_description = "Mark as Published"
    make_pending.short_description = "Mark as Pending"
    make_archive.short_description = "Mark as Archived"
    make_completed.short_description = "Mark as Completed"
    make_delete.short_description = "Mark as Deleted"
    make_complete.short_description = "Mark as Completed"
