from django.shortcuts import render

# Create your views here.
from .models import Book

def book_list_web(request):
    books = Book.objects.all()

    # aram kutuusndan gelen kelimeyi alıyor

    q = request.GET.get('q')

    if q:
        # baslıkta veya yazar kısmında aranan kelimeler filtreler

        books = books.filter(title__icontains=q) | books.filter(author__icontains=q) 

    context ={
        'books':books,
        'arama_kelimesi':q or ''
    }

    return render(request, 'books/book_list.html',context)


