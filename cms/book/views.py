from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('首页')
    
def book(request):
    return HttpResponse('图书首页')

def book_detail(request,book_id):
    text = '你获取的图数是' + book_id
    return HttpResponse(text)