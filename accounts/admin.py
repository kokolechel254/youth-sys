from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomAuthenticationForm, CustomUserCreationForm


User = get_user_model()


class CustomUserAdmin(UserAdmin):
    """Customise the appearence of user in the admin interface

    Args:
        UserAdmin (instance):
        is the original userdmin which is to be extended in this module
    """

    add_form = CustomUserCreationForm
    login_form = CustomAuthenticationForm

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {"fields": ("first_name", "last_name", "email",)},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
