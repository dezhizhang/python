from django.http import HttpResponse
from django.shortcuts import redirect,reverse

def index(request):
    index_url = reverse('index:index')
    print(index_url)
    return HttpResponse('前台首页')

def login(request):
    return HttpResponse('前台登录页')

