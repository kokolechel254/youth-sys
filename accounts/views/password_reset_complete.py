from django.contrib.auth.views import PasswordResetCompleteView


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"
