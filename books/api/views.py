from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from books.models import Book,Category
from .serializers import BookSerializer,CategorySerializer

# All book list (GET) and book add (POST)

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # filtreleme motorlarını tanımlıyoruz
    filter_backends = [
        DjangoFilterBackend, # filtremele / eşleşme
        filters.SearchFilter, # Search Bar
        filters.OrderingFilter, # Sıralama price, date
    ]

    # birebir filtreleme yapılacak alanlar
    filterset_fields = ['category']

    # metin arama yapılacak (title, author)
    search_fields = ['title', 'author']

    ordering_fields = ['id','price', 'publish_date']
    ordering = ['-id']

# a book retrieve (GET) update (PUT) delete (DELETE)
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializer

# Category list and add
class CategoryListCreateApIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer