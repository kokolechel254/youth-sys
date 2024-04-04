from django.contrib.auth.views import PasswordResetConfirmView


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
