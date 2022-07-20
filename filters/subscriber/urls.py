from django.urls import path
from .views import SubscriberView

urlpatterns = [
    path('', SubscriberView.as_view(), name='subscriber/newsletter.html'),
]
