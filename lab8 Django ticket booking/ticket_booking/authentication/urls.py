from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signin),
    path('signup/', views.signup)
]
