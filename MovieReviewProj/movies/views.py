from django.views.generic import TemplateView
class MoviesPageView(TemplateView):
   template_name = 'movies/movies.html'