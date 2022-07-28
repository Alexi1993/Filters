from django.urls import path
from .views import IndexView, NewNewsView, take_new

urlpatterns = [
    path('', IndexView.as_view()),
    path('tasks/', NewNewsView.as_view(), name = 'new_news'),
    path('take/<int:oid>', take_new, name = 'take_new')
]