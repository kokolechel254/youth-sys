from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )


class CustomAuthenticationForm(AuthenticationForm):
    pass


class AccountsForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        pass
