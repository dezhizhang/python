from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):
    book = Book(name='web安全',author='吴大人',price=100)
    book.save()
    return HttpResponse('图书添加成功')

def search(request):
    book = Book.objects.get(pk=1)
    print(book)
    return HttpResponse('查询图书成功')

def update(request):
    book = Book.objects.get(pk=5)
    book.price = 200
    book.save()
    return HttpResponse('更新数据成功')

def delete(request):
    book = Book.objects.filter(name='三国志')
    book.delete()
    return HttpResponse('删除数据成功')





