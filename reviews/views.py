from django.shortcuts import render
from django.core.paginator import Paginator

from reviews.models import Review

# Create your views here.
def reviews_web(request):
    reviews_list = Review.objects.all()

    context = {
        'reviews':reviews_list,
    }

    return render(request, 'reviews/reviews_list.html', {'reviews':reviews_list,})