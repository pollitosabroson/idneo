from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'/search', views.search, name='search'),
    url(r'/([a-zA-Z0-9-]+)$', views.book, name='single-book'),
]
