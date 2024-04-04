from django.contrib.auth.views import PasswordChangeDoneView


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"
