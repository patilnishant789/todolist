from django.shortcuts import render, redirect
from .models import TodoItem


def index(request):
    all_items = TodoItem.objects.all()
    return render(request, 'index.html', {'all_items': all_items})


def add(request):
    item = request.POST['item']
    new_item = TodoItem(item=item)
    new_item.save()
    return redirect('index')


def delete(request, item_id):
    item_to_delete = TodoItem.objects.get(id=item_id).delete()
    return redirect('index')


def deleteAll(request):
    delete_all = TodoItem.objects.all().delete()
    return redirect('index')
