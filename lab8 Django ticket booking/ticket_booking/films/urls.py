from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.films, name="list_films"),
    path('add/', views.add, name="add_film"),
    url(r'^(?P<id>\d+)$', views.itemShow),
]
