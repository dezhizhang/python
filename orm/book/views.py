from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    book = Book(name = '学习笔记',author='张德志',price=10)
    book.save()
    return HttpResponse('图书添加成功')

def search(request):
    book = Book.objects.filter(name='学习笔记')
    print(book)
    return HttpResponse('图书查找成功')

def update(request):
    book = Book.objects.get(pk=6)
    book.price = 100
    book.save()
    return HttpResponse('图书更新成功')
def delete(request):
    book = Book.objects.filter(name='web安全')
    book.delete()
    return HttpResponse('图书删除成功')





