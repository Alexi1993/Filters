from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import *


class AddAuthor(PermissionRequiredMixin, CreateView):
    permission_required = ('subscriber.add_author_name',)


class MyView(PermissionRequiredMixin, View):
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>')


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = get(name='common')
        common_group.user_set.add(user)
        return user
