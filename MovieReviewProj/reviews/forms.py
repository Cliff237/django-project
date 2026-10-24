from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']
        widgets = {
            'rating': forms.Select(attrs={'class': 'btn'}),  # We'll style it as a button-like select? Or use radio?
            'review_text': forms.Textarea(attrs={'rows': 4, 'class': 'field'}),
        }
        labels = {
            'rating': 'Your Rating',
            'review_text': 'Your Review',
        }