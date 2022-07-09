from django_filters import FilterSet
from .models import New


# создаём фильтр
class NewsFilter(FilterSet):
    class Meta:
        model = New
        fields = ['title', 'category', 'author']
