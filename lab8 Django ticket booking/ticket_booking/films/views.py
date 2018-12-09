from django.shortcuts import render, redirect
import json
from cinemas.models import Cinema
from .models import Film, Place, Ceance
from rest_framework.decorators import api_view
import random
from users.models import MyTicket, User

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
    for pl in places:
        Place(place=pl, ceance=ceance).save()
    return redirect("/films/")


def itemShow(request, id):
    user = json.loads(request.session['user'])
    film = Film.objects.get(pk=id)
    ceance = list(Ceance.objects.filter(film=film))
    info = {}
    for item in ceance:
        if not item.cinema in info:
            info[item.cinema] = { item.id: list([item.time,item.price]) }
        else:
            info[item.cinema][item.id] = list([item.time,item.price])
    return render(request, 'films/display.html', {'user':user, 'film':film, 'ceance':info})

def delete(request, filmID, cinemaID):
    film = Film.objects.get(pk=filmID)
    cinema = Cinema.objects.get(pk = cinemaID)
    Ceance.objects.filter(film=film, cinema=cinema).delete()
    return redirect('/cinemas/'+str(cinemaID))

def choose(request, ceanceID):
    user = json.loads(request.session['user'])
    ceance = Ceance.objects.get(pk=ceanceID)
    place = list(Place.objects.filter(ceance=ceance).order_by('place'))
    return render(request, 'films/place.html', {'user':user, 'place':place, 'ceance':ceance})

@api_view(['POST'])
def buy(request):
    user = json.loads(request.session['user'])
    user = User.objects.get(pk=user['id'])
    checkbox = [int(i) for i in request.POST.getlist('places')]
    for item in checkbox:
        temp = Place.objects.get(pk=item)
        temp.status = False
        temp.save()
        MyTicket(user=user, place=temp).save()
    return redirect('/user/myticket/')