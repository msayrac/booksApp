from django.contrib import admin
from reviews.models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','book','rating', 'created_at','updated_at')
    list_filter =('rating','created_at','user')
    search_fields = ('book','user')
    date_hierarchy = 'created_at'

admin.site.register(Review,ReviewAdmin)