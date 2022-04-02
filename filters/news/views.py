from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .filters import *
from .forms import *


class News(ListView):
    model = New
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


class NewDetailView(DetailView):
    model = New
    template_name = 'news/news.html'
    context_object_name = 'news'
    queryset = New.objects.all()


class NewCreateView(CreateView):
    template_name = 'news/create.html'
    form_class = NewForm


class NewUpdateView(UpdateView):
    template_name = 'news/create.html'
    form_class = NewForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return New.objects.get(pk=id)


class NewDeleteView(DeleteView):
    template_name = 'news/delete.html'
    queryset = New.objects.all()
    success_url = '/news/'
