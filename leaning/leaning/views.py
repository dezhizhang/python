from django.shortcuts import render

def index(request):
    # context = {
    #     'colors':['red','yellow','pink','green'],
    #     'person':{
    #         'username':'zhangsan',
    #         'age':18,
    #         'height':180
    #     }
    context = {
       'books':[
           {
               'name':'张三',
               'age':22,
               'height':180
           },
           {
               'name':'李四',
               'age':18,
               'height':160
           },
           {
               'name':'王五',
               'age':16,
               'height':16
           }
       ] 
    }
    return render(request,'index.html',context = context)