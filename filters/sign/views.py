from django.contrib.auth.models import *
from .models import BaseRegisterForm, Subscriber
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.core.mail import *
from datetime import datetime
from django.views.generic import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_managers


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


@receiver(post_save, sender=Subscriber)
def notify_managers(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.authors_name} {instance.date.strftime("%d %m %Y")}'
    else:
        subject = f'Appointment changed for {instance.authors_name} {instance.date.strftime("%d %m %Y")}'
    mail_managers(subject=subject, message=instance.message, )


class SubscriberView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'newsletter.html', {})

    def post(self, request, *args, **kwargs):
        subscriber = Subscriber(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            authors_name=request.POST['authors_name'],
            message=request.POST['message'],
        )
        subscriber.save()

        # отправляем письмо всем админам по аналогии с send_mail, только здесь получателя указывать не надо
        mail_admins(
            subject=f'{subscriber.authors_name} {subscriber.date.strftime("%d %m %Y")}',
            message=subscriber.message,
        )

        return redirect('subscriber:newsletter.html')
