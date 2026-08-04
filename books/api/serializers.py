from rest_framework import serializers
from books.models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','slug']

class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name',read_only=True)

    class Meta:
        model = Book
        fields = ['id','title','author','description','price','stock','publish_date','category','category_name']