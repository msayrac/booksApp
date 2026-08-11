from django.urls import path
from .views import reviews_web

urlpatterns = [
    path('', reviews_web, name='reviews-web'),
]



