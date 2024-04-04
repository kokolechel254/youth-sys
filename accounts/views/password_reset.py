from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomPasswordResetView(PasswordResetView):
    email_template_name = ("accounts/password_reset_email.html",)
    subject_template_name = ("accounts//password_reset_subject.txt",)
    template_name = "accounts/password_reset_form.html"
