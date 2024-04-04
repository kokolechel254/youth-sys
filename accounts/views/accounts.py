from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from accounts.forms import AccountsForm


User = get_user_model()


class UniversalAttributes:
    model = User


class DetailView(UniversalAttributes, generic.DetailView):
    def get_object(self, queryset=None):
        return self.request.user


class CreateView(UniversalAttributes, SuccessMessageMixin, generic.CreateView):
    form_class = AccountsForm
    success_url = reverse_lazy("login")

    def get_context_data(self, *args, **kwargs):
        context = super(CreateView, self).get_context_data(*args, **kwargs)
        context["page_title"] = "New Account"
        return context


class UpdateView(UniversalAttributes, generic.UpdateView):
    form_class = AccountsForm
