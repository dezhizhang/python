from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


def get_corsor():
    return connection.corsor()


def index(request):
    
    return render(request,'index.html')


def add_book(request):
    return render(request,'add_book.html')

def book_detail(request,book_id):
    return render(request,'book_detail.html')





