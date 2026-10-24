from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse

from movies.models import Movie
from .models import Review


def make_user(self, username):
    from django.contrib.auth.models import User
    return User.objects.create(
        username=username,
        password=make_password('Tr0ub4dor&3'),
    )


class ReviewsPageTest(TestCase):
    def test_list_page_200(self):
        response = self.client.get(reverse('reviews-list'))
        self.assertEqual(response.status_code, 200)


class AddReviewViewTest(TestCase):
    def setUp(self):
        self.user = make_user(self, 'alice')
        self.movie = Movie.objects.create(title='Dune')

    def test_add_requires_login(self):
        response = self.client.post(reverse('reviews-add'), {
            'movie_id': self.movie.id,
            'rating': 5,
            'review_text': 'Great!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)
        self.assertEqual(Review.objects.count(), 0)

    def test_add_review_success(self):
        self.client.login(username='alice', password='Tr0ub4dor&3')
        response = self.client.post(reverse('reviews-add'), {
            'movie_id': self.movie.id,
            'rating': 5,
            'review_text': 'Great!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('movie-detail', kwargs={'slug': 'dune'}))
        self.assertEqual(Review.objects.count(), 1)

    def test_duplicate_review_rejected(self):
        self.client.login(username='alice', password='Tr0ub4dor&3')
        self.client.post(reverse('reviews-add'), {
            'movie_id': self.movie.id, 'rating': 4, 'review_text': 'First.',
        })
        self.client.post(reverse('reviews-add'), {
            'movie_id': self.movie.id, 'rating': 2, 'review_text': 'Second.',
        })
        self.assertEqual(Review.objects.count(), 1)

    def test_rating_out_of_range_rejected(self):
        self.client.login(username='alice', password='Tr0ub4dor&3')
        self.client.post(reverse('reviews-add'), {
            'movie_id': self.movie.id, 'rating': 9, 'review_text': 'Boom.',
        })
        self.assertEqual(Review.objects.count(), 0)


class EditDeleteReviewTest(TestCase):
    def setUp(self):
        self.owner = make_user(self, 'alice')
        self.other = make_user(self, 'bob')
        self.movie = Movie.objects.create(title='Dune')
        self.review = Review.objects.create(
            user=self.owner, movie=self.movie, rating=3, review_text='OK.',
        )

    def test_edit_requires_login(self):
        response = self.client.get(reverse('reviews-edit', kwargs={'pk': self.review.pk}))
        self.assertEqual(response.status_code, 302)

    def test_edit_failed_invisible_to_other_users(self):
        self.client.login(username='bob', password='Tr0ub4dor&3')
        response = self.client.get(reverse('reviews-edit', kwargs={'pk': self.review.pk}))
        self.assertEqual(response.status_code, 404)

    def test_owner_can_edit(self):
        self.client.login(username='alice', password='Tr0ub4dor&3')
        response = self.client.post(reverse('reviews-edit', kwargs={'pk': self.review.pk}), {
            'rating': 5, 'review_text': 'Better on rewatch.',
        })
        self.assertEqual(response.status_code, 302)
        self.review.refresh_from_db()
        self.assertEqual(self.review.rating, 5)

    def test_delete_failed_invisible_to_other_users(self):
        self.client.login(username='bob', password='Tr0ub4dor&3')
        response = self.client.post(reverse('reviews-delete', kwargs={'pk': self.review.pk}))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Review.objects.filter(pk=self.review.pk).exists())

    def test_owner_can_delete(self):
        self.client.login(username='alice', password='Tr0ub4dor&3')
        response = self.client.post(reverse('reviews-delete', kwargs={'pk': self.review.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Review.objects.filter(pk=self.review.pk).exists())
