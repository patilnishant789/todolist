from django.db import models
from tastypie.resources import ModelResource
from task.models import TodoItem

class TodoitemResource(ModelResource):
    class Meta:
        queryset = TodoItem.objects.all()
        resource_name = 'todo'