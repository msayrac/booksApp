from django.urls import path
from reviews.api.views import ReviewListCreateAPIView,ReviewDetailAPIView

urlpatterns = [
    path('reviews/', ReviewListCreateAPIView.as_view(), name='api-review-list'),
    path('reviews/<int:pk>/',ReviewDetailAPIView.as_view(), name='api-review-detail')
]