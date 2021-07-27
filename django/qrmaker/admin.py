from django.contrib import admin
from .models import *


class PromoAdmin(admin.ModelAdmin):
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

    def make_published(self, request, queryset):
        queryset.update(state="Published")

    make_published.short_description = "Mark as Published"

    def make_pending(self, request, queryset):
        queryset.update(state="Pending")

    make_pending.short_description = "Mark as Pending"

    def make_archive(self, request, queryset):
        queryset.update(state="Archived")

    make_archive.short_description = "Mark as Archived"

    def make_delete(self, request, queryset):
        queryset.update(state="Deleted")

    make_delete.short_description = "Mark as Deleted"

    def make_complete(self, request, queryset):
        queryset.update(state="Completed")

    make_complete.short_description = "Mark as Completed"


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
