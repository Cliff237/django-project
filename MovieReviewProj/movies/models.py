from django.db import models
from django.utils.text import slugify


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    poster = models.ImageField(
        upload_to='movie_posters/', blank=True, null=True)
    trailer_url = models.URLField(blank=True, null=True, 
                                  help_text="YouTube embed link (optional)")
    trailer_video = models.FileField(upload_to='movie_trailers/', 
                                     blank=True, null=True,
                                     help_text="Upload video file (mp4, webm) - optional")
    description = models.TextField()
    release_date = models.DateField()
    movie_type = models.CharField(max_length=20, choices=[
        ('movie', 'Movie'),
        ('series', 'Series'),
        ('animation', 'Animation'),
    ], default='movie')
    genres = models.ManyToManyField(Genre, related_name='movies')
    duration = models.PositiveIntegerField(
        help_text="Duration in minutes", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-release_date', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
