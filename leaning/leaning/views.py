from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


def get_cursor():
    return connection.cursor()


def index(request):
    cursor = get_cursor()
    cursor.execute('select id,name,author from book')
    books = cursor.fetchall()
    return render(request,'index.html',context={'books':books})


def add_book(request):
    return render(request,'add_book.html')

def book_detail(request,book_id):
    return render(request,'book_detail.html')





