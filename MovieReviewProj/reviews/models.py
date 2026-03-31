from django.db import models
from django.conf import settings
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Commented for now
    reviewer_name = models.CharField(max_length=100, default="Anonymous")  # Temporary field
    rating = models.PositiveSmallIntegerField(choices=[(i, f"{i} Stars") for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        # unique_together = ['movie', 'user']  # Will activate later

    def __str__(self):
        return f"{self.reviewer_name} - {self.movie.title} ({self.rating}★)"
    
    def get_stars(self):
        """Helper to display filled stars"""
        return '★' * self.rating + '☆' * (5 - self.rating)