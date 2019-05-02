from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


def index(request):
    cursor = connection.cursor()
    cursor.execute("insert into user(id,name,age) values(null,'张三',22)")
    return render(request,'index.html')




