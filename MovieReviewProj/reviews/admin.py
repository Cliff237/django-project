from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Review


@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ('movie', 'reviewer_name', 'rating', 'created_at', 'short_comment')
    list_filter = ('rating', 'created_at', 'movie')
    search_fields = ('movie__title', 'reviewer_name', 'comment')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    def short_comment(self, obj):
        return (obj.comment[:80] + "...") if len(obj.comment) > 80 else obj.comment
    short_comment.short_description = 'Comment'