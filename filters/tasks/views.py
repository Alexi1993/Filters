from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from .tasks import complete_order
from .models import New
from datetime import datetime


# главная страница - таблица заказов
class IndexView(TemplateView):
    template_name = "tasks/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = New.objects.all()
        return context


# форма нового заказа
class NewNewsView(CreateView):
    model = New
    fields = ['category']  # единственное поле
    template_name = 'tasks/main.html'

    # после валидации формы, сохраняем объект,
    # считаем его общую стоимость
    # и вызываем задачу "завершить заказ" через минуту после вызова
    def form_valid(self, form):
        news = form.save()
        New.cost = sum([category.price for category in New.products.all()])
        New.save()
        complete_order.apply_async([New.pk], countdown=60)
        return redirect('/')


# представление для "кнопки", чтобы можно было забрать заказ
def take_new(request, oid):
    news = New.objects.get(pk=oid)
    New.time_out = datetime.now()
    New.save()
    return redirect('/')
