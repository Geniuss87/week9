from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog


def get_hello(request):
    return HttpResponse("test!")


def index_page(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', locals())


def detail_page(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'detail.html', locals())