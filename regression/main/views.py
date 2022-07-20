from django.shortcuts import render
from django.http  import HttpResponse
from .models import ToDolist, Item

# Create your views here.

def index(response):
    return HttpResponse('<h1> Hi, this is my first view </h1>')

def query(response, id):
    ls = ToDolist.objects.get(id = id)
    item = ls.item_set.get(id = id)
    return HttpResponse('<h1>%s</h1><br></br><p>%s</p>' %(ls.name, str(item.text)))

