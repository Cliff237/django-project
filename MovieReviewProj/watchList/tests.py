from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse

from movies.models import Movie
from .models import WatchListItem


def make_user(username):
    from django.contrib.auth.models import User
    return User.objects.create(
        username=username,
        password=make_password('Tr0ub4dor&3'),
    )


class WatchListModelTest(TestCase):
    def test_str_represents_pair(self):
        user = make_user('alice')
        movie = Movie.objects.create(title='Dune')
        item = WatchListItem.objects.create(user=user, movie=movie)
        self.assertEqual(str(item), 'alice - Dune')

    def test_unique_per_user_movie(self):
        user = make_user('alice')
        movie = Movie.objects.create(title='Dune')
        WatchListItem.objects.create(user=user, movie=movie)
        with self.assertRaises(Exception):
            WatchListItem.objects.create(user=user, movie=movie)


class WatchListToggleViewTest(TestCase):
    def setUp(self):
        self.user = make_user('alice')
        self.movie = Movie.objects.create(title='Dune')

    def test_toggle_requires_login(self):
        response = self.client.post(reverse('watchlist-toggle'), {'movie_id': self.movie.id})
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)
        self.assertEqual(WatchListItem.objects.count(), 0)

    def test_toggle_adds_then_removes(self):
        self.client.login(username='alice', password='Tr0ub4dor&3')
        self.client.post(reverse('watchlist-toggle'), {'movie_id': self.movie.id})
        self.assertTrue(
            WatchListItem.objects.filter(user=self.user, movie=self.movie).exists()
        )
        self.client.post(reverse('watchlist-toggle'), {'movie_id': self.movie.id})
        self.assertFalse(
            WatchListItem.objects.filter(user=self.user, movie=self.movie).exists()
        )


class WatchListPageTest(TestCase):
    def setUp(self):
        self.user = make_user('alice')
        self.movie = Movie.objects.create(title='Dune')

    def test_page_requires_login(self):
        response = self.client.get(reverse('watchlist'))
        self.assertEqual(response.status_code, 302)

    def test_page_shows_only_own_items(self):
        bob = make_user('bob')
        WatchListItem.objects.create(user=self.user, movie=self.movie)
        other_movie = Movie.objects.create(title='Interstellar')
        WatchListItem.objects.create(user=bob, movie=other_movie)

        self.client.login(username='alice', password='Tr0ub4dor&3')
        response = self.client.get(reverse('watchlist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dune')
        self.assertNotContains(response, 'Interstellar')

        self.client.login(username='alice', password='Tr0ub4dor&3')
        response = self.client.get(reverse('watchlist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dune')
        self.assertNotContains(response, 'Interstellar')
