from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {

    }
    return render(request,'index.html',context = context)

def book(request):
    return HttpResponse('读书')

def movie(request):
    return HttpResponse('电影')

def city(request):
    return HttpResponse('同城')


