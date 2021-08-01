from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import AccountCreationForm, AccountChangeForm


class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account

    list_display = (
        "email",
        "date_joined",
        "last_login",
        "is_admin",
        "is_staff",
    )
    search_fields = ("email",)
    readonly_fields = ("date_joined", "last_login")
    ordering = ("email",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )


admin.site.register(Account, AccountAdmin)
