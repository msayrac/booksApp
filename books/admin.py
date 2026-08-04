from django.contrib import admin

# Register your models here.
from books.models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','price','stock','publish_date','category')
    list_filter = ('author','publish_date','title','price')
    search_fields = ('title','author','price','stock')

    date_hierarchy = 'publish_date'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)



admin.site.register(Category,CategoryAdmin)
admin.site.register(Book,BookAdmin)