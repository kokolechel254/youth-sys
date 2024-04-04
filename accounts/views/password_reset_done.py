from django.contrib.auth.views import PasswordResetDoneView


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"
