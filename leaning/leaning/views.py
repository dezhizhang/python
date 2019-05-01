from django.shortcuts import render

def index(request):
    context = {
        'age':18
    }
    return render(request,'index.html',context = context)