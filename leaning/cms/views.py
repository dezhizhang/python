from django.http import HttpResponse

def index(request):
    return HttpResponse('后台首页')

def login(request):
    return HttpResponse('后台登录页')
