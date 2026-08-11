from rest_framework import generics
from reviews.models import Review
from reviews.api.serializers import ReviewSerializer

class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Review.objects.all()
    serializer_class =ReviewSerializer