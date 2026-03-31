from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'reviewer_name', 'rating', 'created_at']
    list_filter = ['rating', 'created_at', 'movie']
    search_fields = ['movie__title', 'reviewer_name', 'comment']
    readonly_fields = ['created_at', 'updated_at']