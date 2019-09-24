from django.db import models


class TodoItem(models.Model):
    item = models.TextField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item
