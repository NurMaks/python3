from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("authentication.urls")),
    path('auth/', include("authentication.urls")),
    path('user/', include("users.urls")),
    path('films/', include('films.urls')),
    path('cinemas/', include('cinemas.urls')),
]
