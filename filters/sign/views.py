from django.contrib.auth.models import *
from .models import BaseRegisterForm
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.views.generic import *


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')
