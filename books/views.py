from django.shortcuts import render

# Create your views here.
from .models import Book

def book_list_web(request):
    books = Book.objects.all()

    context ={
        'books':books
    }

    return render(request, 'books/book_list.html',context)


