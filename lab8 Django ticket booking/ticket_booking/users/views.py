from django.shortcuts import render, redirect
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from rest_framework.decorators import api_view
from .forms import UserSigninForms, UserSignupForm
from .models import User, MyTicket
from .serializers import UserSerializer
import json
def convertToDict(user):
    data = {
        'id': user.id,
        'name': user.fname+" "+user.lname,
        'email': user.email,
        'priority': user.priority
    }
    return data

def createSession(request, form):
    user = None
    try:
        user = User.objects.get(email=form['email'].value(), password=form['password'].value())
    except:
        return False
    user = json.dumps(convertToDict(user))
    request.session['user'] = user
    return True

@api_view(['POST'])
def signin(request):
    form = UserSigninForms(request.POST)
    if not form.is_valid():
        return render(request, 'signin/signin.html', status=HTTP_400_BAD_REQUEST)
    if not createSession(request, form):
        return render(request, 'signin/signin.html', {'error':"User not found!"}, status=HTTP_404_NOT_FOUND)
    return redirect('/films/')

@api_view(['POST'])
def signup(request):
    form = UserSignupForm(request.POST)
    if User.objects.filter(email=form['email'].value()):
        return render(request, 'signup/signup.html', {'error':"This login is already in use!"})
    user = UserSerializer(data = request.data)
    if not user.is_valid():
        return render(user.errors, 'signup/signup.html', status=HTTP_400_BAD_REQUEST)
    user.save()
    createSession(request, form)
    return redirect('/films/')
    
def myticket(request):
    user = json.loads(request.session['user'])
    ticket = MyTicket.objects.filter(user=User.objects.get(pk=user['id']))
    return render(request, 'myticket/myticket.html', {'user':user, 'ticket':ticket})