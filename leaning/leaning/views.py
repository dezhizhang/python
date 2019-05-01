from django.shortcuts import render

def index(request):
    context = {
        'person':['哈哈哈','嘿嘿','呀呀呢']
    }
    return render(request,'index.html',context = context)