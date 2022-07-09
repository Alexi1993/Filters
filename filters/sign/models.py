from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import *
from django.db import models
from datetime import datetime


class Subscriber(models.Model):
    date = models.DateField(default=datetime.utcnow)
    authors_name = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'{self.authors_name}: {self.message}'


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
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
