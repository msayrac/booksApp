from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Book

def book_list_web(request):
    books_list = Book.objects.all().order_by('-id')

    # aram kutuusndan gelen kelimeyi alıyor

    q = request.GET.get('q')
    if q:
        # baslıkta veya yazar kısmında aranan kelimeler filtreler
        books_list = books_list.filter(title__icontains=q) | books_list.filter(author__icontains=q)

    paginator = Paginator(books_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    # context ={
    #     'books':books,
    #     'arama_kelimesi':q or ''
    # }

    return render(request, 'books/book_list.html',{'books':page_obj, 'arama_kelimesi':q or ''})


