from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock =models.IntegerField(default=10)
    publish_date = models.DateField(auto_now_add=True)
    category =models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'books')

    class Meta:
        verbose_name_plural = 'Books'

    def __str__(self):
        return f'{self.title} - {self.author}'
