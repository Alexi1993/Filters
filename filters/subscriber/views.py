from .models import Subscriber
from django.shortcuts import redirect
from django.core.mail import *
from django.views import View
from datetime import datetime


class SubscriberView(View):

    def post(request, self, **kwargs):
        subscriber = Subscriber(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            authors_name=request.POST['authors_name'],
            message=request.POST['message'],
        )
        subscriber.save()

        mail_admins(
            subject=f'{subscriber.authors_name} {subscriber.date.strftime("%d %m %Y")}',
            message=subscriber.message,
        )

        return redirect('subscriber:newsletter.html')
