from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from books.models import Book

# Create your models here.
class Review(models.Model):
    book =models.ForeignKey(Book,on_delete=models.CASCADE, related_name='reviews')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)

    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.book.title} - {self.rating} Star'