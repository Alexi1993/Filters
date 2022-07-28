from django.db import models


class New(models.Model):
    title = models.CharField(max_length=64, null=True, blank=True)
    text = models.TextField(max_length=356, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.title} {self.author}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
