from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from django.db.models import Avg, Count

from .models import Genre, Movie
from reviews.models import Review


# ===================== GENRE ADMIN =====================
@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ('name', 'movie_count')
    search_fields = ('name',)

    def movie_count(self, obj):
        return obj.movies.count()
    movie_count.short_description = 'Number of Movies'


# ===================== MOVIE ADMIN =====================
@admin.register(Movie)
class MovieAdmin(ModelAdmin):
    list_display = ('title', 'movie_type', 'release_date', 'duration', 
                    'poster_preview', 'review_count', 'avg_rating')
    list_filter = ('movie_type', 'genres', 'release_date')
    search_fields = ('title', 'description')
    ordering = ('-release_date', 'title')
    filter_horizontal = ('genres',)   # Better UI for many-to-many

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'release_date', 'movie_type', 'duration')
        }),
        ('Media', {
            'fields': ('poster', 'trailer_url', 'trailer_video')
        }),
        ('Genres', {
            'fields': ('genres',)
        }),
    )

    def poster_preview(self, obj):
        if obj.poster:
            return format_html(
                '<img src="{}" width="60" style="border-radius: 6px; object-fit: cover;" />', 
                obj.poster.url
            )
        return "-"
    poster_preview.short_description = 'Poster'

    def review_count(self, obj):
        return obj.reviews.count()
    review_count.short_description = 'Reviews'

    def avg_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            avg = sum(r.rating for r in reviews) / len(reviews)
            return f"{avg:.1f} ★"
        return "—"
    avg_rating.short_description = 'Avg Rating'


# ===================== DASHBOARD CALLBACK =====================
def dashboard_callback(request, context):
    """Custom statistics for Unfold Admin Dashboard"""
    total_movies = Movie.objects.count()
    total_reviews = Review.objects.count()
    avg_rating_all = Review.objects.aggregate(avg=Avg('rating'))['avg'] or 0
    
    recent_movies = Movie.objects.order_by('-created_at')[:5]
    most_reviewed = Movie.objects.annotate(
        review_count=Count('reviews')
    ).order_by('-review_count')[:5]

    context.update({
        "total_movies": total_movies,
        "total_reviews": total_reviews,
        "avg_rating_all": round(avg_rating_all, 1),
        "recent_movies": recent_movies,
        "most_reviewed": most_reviewed,
    })
    return context