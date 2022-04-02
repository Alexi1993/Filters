from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import New


class NewForm(ModelForm):
    check_box = BooleanField(label='Please, mark!')  # добавляем галочку, или же true-false поле

    class Meta:
        model = New
        fields = ['title', 'category', 'author', 'text', 'check_box']