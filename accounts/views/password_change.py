from django.contrib.auth.views import PasswordChangeView


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "accounts/password_change_form.html"
