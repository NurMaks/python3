from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .models import Cinema
from films.models import Ceance, Film
from .serializers import CinemaSerializer
import json
from django import forms

def cinemas(request):
    user = json.loads(request.session['user'])
    cinema_list = list(Cinema.objects.all())
    return render(request, 'cinemas/cinemas.html', {'user':user, 'cinema':cinema_list})

@api_view(['POST'])
def add_cinema(request):
    cinema = CinemaSerializer(data = request.data)
    if not cinema.is_valid():
        return render(cinema.errors, 'cinemas/cinemas.html')
    cinema.save()
    return redirect("/cinemas/")

def item(request, id):
    user = json.loads(request.session['user'])
    cinema = Cinema.objects.get(pk=id)
    film = {}
    for item in Ceance.objects.filter(cinema=cinema):
        if item.film not in film:
            film[item.film] = { item.id: [item.time,item.price] }
        else:
            film[item.film][item.id] = [item.time,item.price]
    return render(request, 'cinema/item.html', {'user':user, 'cinema':cinema, 'film':film})

def delete(request, id):
    cinema = Cinema.objects.get(pk=id)
    cinema.delete()
    return redirect("/cinemas/")
