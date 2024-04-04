from django.contrib.auth.views import LoginView
from accounts.forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = CustomAuthenticationForm
