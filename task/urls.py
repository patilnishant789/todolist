from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete/<item_id>', views.delete, name='delete'),
    path('deleteAll', views.deleteAll, name='deleteAll')
]