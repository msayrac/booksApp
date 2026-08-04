from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView, CategoryListCreateApIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='api-book-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='api-book-detail'),
    path('categories/',CategoryListCreateApIView.as_view(), name='api-category-list'),
]