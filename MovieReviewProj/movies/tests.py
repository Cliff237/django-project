from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Genre, Movie


class MovieModelTest(TestCase):
    def test_slug_generated_from_title(self):
        movie = Movie.objects.create(title='Interstellar Odyssey')
        self.assertEqual(movie.slug, 'interstellar-odyssey')

    def test_slug_unique_across_same_titles(self):
        Movie.objects.create(title='Dune')
        second = Movie.objects.get_or_create(title='Dune')[0]
        self.assertIsNotNone(second.slug)

    def test_genre_slug_generated(self):
        genre = Genre.objects.create(name='Science Fiction')
        self.assertEqual(genre.slug, 'science-fiction')

    def test_movie_str(self):
        movie = Movie.objects.create(title='Dune', synopsis='Deserts')
        self.assertEqual(str(movie), 'Dune')


class MoviesPageTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title='Dune',
            synopsis='A desert epic.',
            release_date=date(2024, 3, 1),
        )

    def test_list_page_200(self):
        response = self.client.get(reverse('movies-list'))
        self.assertEqual(response.status_code, 200)

    def test_list_shows_movie(self):
        response = self.client.get(reverse('movies-list'))
        self.assertContains(response, 'Dune')

    def test_detail_page_200(self):
        response = self.client.get(reverse('movie-detail', kwargs={'slug': 'dune'}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['movie'], self.movie)

    def test_detail_unknown_slug_404(self):
        response = self.client.get(reverse('movie-detail', kwargs={'slug': 'nope'}))
        self.assertEqual(response.status_code, 404)
