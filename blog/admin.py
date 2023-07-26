from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_view', 'status', 'published_date', 'created_at')
    list_filter = ('status',)
    ordering = ['-created_at']
    search_fields = ['title', 'counted_view']
    summernote_fields = ('content',)

admin.site.register(Category)