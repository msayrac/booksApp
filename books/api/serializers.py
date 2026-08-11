from rest_framework import serializers
from books.models import Book, Category
from reviews.api.serializers import ReviewSerializer
from reviews.models import Review

class CategorySimpleSerializer(serializers.ModelSerializer):
    # books = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','slug']

class BookReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model = Review
        fields =['id','username','rating','comment','created_at']


class BookSerializer(serializers.ModelSerializer):
    category_detail = CategorySimpleSerializer(source='category', read_only =True)
    # category_name = serializers.CharField(source='category.name',read_only=True)

    # reviews = ReviewSerializer(many=True, read_only=True)
    reviews = BookReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id','title','author','description','price','stock','publish_date','category','category_detail','reviews']

class CategorySerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','slug','books']