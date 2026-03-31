from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from movies.models import Movie
from reviews.models import Review

User = get_user_model()

class ReviewModelTests(TestCase):
    def setUp(self):
        # create a user and movie to relate reviews to
        self.user = User.objects.create_user(username='tester', password='pass')
        self.movie = Movie.objects.create(
            title='Test Movie',
            description='A movie used for tests.',
            release_year=2020
        )

    def test_create_review_with_valid_fields(self):
        """Should create a Review instance with valid fields."""
        r = Review.objects.create(
            movie=self.movie,
            user=self.user,
            rating=4,
            text='Great movie!'
        )
        self.assertIsNotNone(r.pk)
        self.assertEqual(r.movie, self.movie)
        self.assertEqual(r.user, self.user)
        self.assertEqual(r.rating, 4)
        self.assertEqual(r.text, 'Great movie!')

    def test_text_field_max_length_validation(self):
        """Should enforce max length / validation for text fields."""
        # Determine if Review.text has a max_length, and test accordingly.
        max_len = None
        try:
            max_len = Review._meta.get_field('text').max_length
        except Exception:
            max_len = None

        if max_len:
            long_text = 'x' * (max_len + 1)
            r = Review(
                movie=self.movie,
                user=self.user,
                rating=3,
                text=long_text
            )
            # full_clean should raise ValidationError for too-long text
            with self.assertRaises(ValidationError):
                r.full_clean()
        else:
            # If no max_length defined, ensure saving large text works
            long_text = 'x' * 20000
            r = Review.objects.create(
                movie=self.movie,
                user=self.user,
                rating=3,
                text=long_text
            )
            self.assertEqual(r.text, long_text)

    def test_timestamps_set_on_save_if_present(self):
        """Should set created/modified timestamps on save if model defines them."""
        r = Review.objects.create(
            movie=self.movie,
            user=self.user,
            rating=5,
            text='Timestamp test'
        )
        # If fields exist, they should be non-null
        if hasattr(r, 'created'):
            self.assertIsNotNone(r.created)
        if hasattr(r, 'modified'):
            self.assertIsNotNone(r.modified)
        # Some models use created_at/updated_at naming
        if hasattr(r, 'created_at'):
            self.assertIsNotNone(r.created_at)
        if hasattr(r, 'updated_at'):
            self.assertIsNotNone(r.updated_at)

    def test_association_and_query_by_movie(self):
        """Should associate a Review with a Movie and allow querying by movie."""
        r1 = Review.objects.create(movie=self.movie, user=self.user, rating=4, text='One')
        r2 = Review.objects.create(movie=self.movie, user=self.user, rating=2, text='Two')
        reviews_qs = Review.objects.filter(movie=self.movie)
        self.assertIn(r1, reviews_qs)
        self.assertIn(r2, reviews_qs)
        self.assertEqual(reviews_qs.count(), 2)

    def test_str_representation(self):
        """Should compute or expose a readable representation for display."""
        r = Review.objects.create(movie=self.movie, user=self.user, rating=3, text='Representation')
        # Prefer __str__, fallback to repr
        s = str(r)
        self.assertIsInstance(s, str)
        self.assertTrue(len(s) > 0)
