from django.db import models
from datetime import datetime


class Subscriber(models.Model):
    date = models.DateField(default=datetime.utcnow)
    authors_name = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'{self.authors_name}: {self.message}'


