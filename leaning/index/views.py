from django.http import HttpResponse

def index(request):
    return HttpResponse('前台首页')

def login(request):
    return HttpResponse('前台登录页')
    
