from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import item


# Create your views here.
def index(request):
    items_list = item.objects.all()
    context = {
    'items_list':items_list,
    }
    return render(request,'home.html',context)


def sanath(request):
    return HttpResponse('Hello sanath')

@login_required
def item_detail(request,item_id):
    item_de = item.objects.get(pk=item_id)
    context = {
        'item':item_de,
    }
    return render(request, 'item_detail.html', context)
