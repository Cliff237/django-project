# from django.contrib import admin

# from .models import Genre, Movie, ProductionCompany, Review

# admin.site.register(Genre)
# admin.site.register(ProductionCompany)
# admin.site.register(Movie)
# admin.site.register(Review)
# # Register your models here

from django.contrib import admin
from .models import Genre, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'movie_type', 'release_date', 'duration']
    list_filter = ['movie_type', 'genres', 'release_date']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}   # auto slug
    filter_horizontal = ['genres']               # nice widget for many-to-many

    # Optional: make poster and trailer nicer in admin
    readonly_fields = ['created_at', 'updated_at']