from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.views import generic
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView

USER_MODEL = get_user_model()


class ProfileView(generic.DetailView):
    model = USER_MODEL
    template_name = "users/profile.html"
    # context_object_name = 'user'


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/createAccount.html"


class MyStoriesView(generic.TemplateView):
    template_name = "users/mystories.html"


class EditAccountInfo(generic.UpdateView):
    fields = "__all__"
    template_name = "users/editAccount.html"
