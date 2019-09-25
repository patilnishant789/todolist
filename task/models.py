from django.db import models
from datetime import datetime


class TodoItem(models.Model):
    item = models.CharField(max_length=15)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.item
