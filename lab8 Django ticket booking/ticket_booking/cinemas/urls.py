from django.urls import path
from django.conf.urls import url
from . import views
from .models import Cinema

urlpatterns = [
    path('', views.cinemas, name="list_cinemas"),
    path('add/', views.add_cinema, name='add_cinema'),
    url(r'^(?P<id>\d+)$', views.item),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]


#DetailView.as_view(model=Cinema, template_name="cinema/item.html")