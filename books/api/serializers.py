from rest_framework import serializers
from books.models import Book, Category


class CategorySimpleSerializer(serializers.ModelSerializer):
    # books = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','slug']

class BookSerializer(serializers.ModelSerializer):
    category_detail = CategorySimpleSerializer(source='category', read_only =True)
    # category_name = serializers.CharField(source='category.name',read_only=True)

    class Meta:
        model = Book
        fields = ['id','title','author','description','price','stock','publish_date','category','category_detail']

class CategorySerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','slug','books']