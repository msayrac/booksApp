from rest_framework import generics
from books.models import Book,Category
from .serializers import BookSerializer,CategorySerializer

# All book list (GET) and book add (POST)

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# a book retrieve (GET) update (PUT) delete (DELETE)
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer

# Category list and add
class CategoryListCreateApIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer