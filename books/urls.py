from django.urls import path
from .views import book_list_web

urlpatterns = [
    path('', book_list_web, name='book-list-web'),
]



