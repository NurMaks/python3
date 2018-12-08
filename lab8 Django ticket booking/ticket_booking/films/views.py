from django.shortcuts import render, redirect
import json
from cinemas.models import Cinema
from .models import Film, Place, Ceance
from rest_framework.decorators import api_view
import random

def films(request):
    user = request.session['user']
    user = json.loads(user)
    cinema = list(Cinema.objects.all())
    film = list(Film.objects.all())
    error = False
    errorMessage = None
    if 'errorSelectedFilmType' in request.session:
        error = True
        errorMessage = "Please, select film or create new!"
        del request.session['errorSelectedFilmType']
    elif 'errorSelectedCinema' in request.session:
        error = True
        errorMessage = "Please, select cinema!"
        del request.session['errorSelectedCinema']
    elif 'errorSelectedInfo' in request.session:
        error = True
        errorMessage = "Please, enter all inputs!"
        del request.session['errorSelectedInfo']
    return render(request, 'films/films.html', {'user': user, 'cinema':cinema, 'film':film, 'errorType':error, 'errorMessage': errorMessage})

@api_view(['POST'])
def add(request):
    data = request.POST.dict()
    if (int(data['selectedFilmID'])!=-1 and data['filmName']) or (int(data['selectedFilmID'])==-1 and not data['filmName']):
        request.session['errorSelectedFilmType'] = True
        return redirect("/films/")
    elif int(data['cinemaID']) == -1:
        request.session['errorSelectedCinema'] = True
        return redirect("/films/")
    elif not data['time'] or not data['price']:
        request.session['errorSelectedInfo'] = True
        return redirect("/films/")
    
    film = None
    if data['filmName']:
        try:
            film = Film.objects.get(name=data['filmName'])
        except:
            Film(name=data['filmName'], image=data['image']).save()
            film = Film.objects.get(name=data['filmName'])
    else:
        film = Film.objects.get(pk=data['selectedFilmID'])
    cinema = Cinema.objects.get(pk=data['cinemaID'])
    Ceance(time=data['time'], price=data['price'], film=film, cinema=cinema).save()
    ceance = Ceance.objects.get(time=data['time'], price=data['price'], film=film, cinema=cinema)
    places = list(range(1, 16))
    randPlaces = places
    randInt = random.randint(1, 10)
    random.shuffle(randPlaces)
    randPlaces = randPlaces[:randInt]
    for pl in places:
        st = True
        if pl in randPlaces:
            st = False
        Place(place=pl, status=st, ceance=ceance).save()
    return redirect("/films/")


def itemShow(request, id):
    user = json.loads(request.session['user'])
    film = Film.objects.get(pk=id)
    ceance = Ceance.objects.get(film=film)