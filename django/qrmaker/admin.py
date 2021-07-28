from django.contrib import admin
from .models import *

from qrmaker.extra import PromoActionChoices


class PromoAdmin(admin.ModelAdmin, PromoActionChoices):
    list_display = ("title", "maker", "date_added", "state")
    search_fields = ("uid", "state", "title")
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ("state", "maker")
    fieldsets = ()
    actions = [
        "make_published",
        "make_pending",
        "make_archive",
        "make_delete",
        "make_complete",
    ]


class MakerAdmin(admin.ModelAdmin):
    list_display = ("username", "uid", "date_added")
    search_fields = ("username", "uid")
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class PromoInstanceAdmin(admin.ModelAdmin):
    list_display = ("title", "promo", "date_added")
    search_fields = ("promo", "title")
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("title", "pinstance", "date_added")
    search_fields = ("pinstance", "title")
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Maker, MakerAdmin)
admin.site.register(Promo, PromoAdmin)
admin.site.register(PromoInstance, PromoInstanceAdmin)
admin.site.register(Transaction, TransactionAdmin)
