from django.urls import path
from .views import *

urlpatterns = [
    path('', News.as_view(), name='news_list'),
    path('<int:pk>/', NewDetailView.as_view(), name='news'),  # Ссылка на детали товара
    path('create/', NewCreateView.as_view(), name='create'),  # Ссылка на создание товара
    path('create/<int:pk>/', NewUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NewDeleteView.as_view(), name='delete'),
]
