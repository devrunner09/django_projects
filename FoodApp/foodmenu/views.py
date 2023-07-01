from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item 
from django.template import loader
from .forms import ItemForm

# Create your views here.
def index(request):
    # template = loader.get_template('foodmenu/index.html')
    item_list = Item.objects.all()
    context = {
        'item_list' : item_list
    }
    return render(request, 'foodmenu/index.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item' : item, 
    }
    return render(request, 'foodmenu/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('foodmenu:index')
    return render(request, 'foodmenu/item-form.html', {'form' : form})

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('foodmenu:index')
    return render(request, 'foodmenu/item-form.html', {'form':form, 'item': item})

def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('foodmenu:index')
    return render(request, 'foodmenu/item-delete.html', {'item':item})