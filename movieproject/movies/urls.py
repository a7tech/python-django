from django.conf.urls import include, url
from movies.views import MoviesHome, Moviesfunctions

urlpatterns = [
    url(r'^$', MoviesHome.as_view()),
    url(r'^loadpage/$', Moviesfunctions.as_view()),
]
