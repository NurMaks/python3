from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from rest_framework.decorators import api_view
from .forms import UserSigninForms, UserSignupForm
from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
def signin(request):
    form = UserSigninForms(request.POST)
    if not form.is_valid():
        return render(request, 'signin/signin.html', status=HTTP_400_BAD_REQUEST)
    user = User.objects.filter(email=form['email'].value(), password=form['password'].value())
    if not user:
        return render(request, 'signin/signin.html', {'error':"User not found!"}, status=HTTP_404_NOT_FOUND)
    #user.first()
    return render(request, 'signup/signup.html', status=HTTP_200_OK)

@api_view(['POST'])
def signup(request):
    form = UserSignupForm(request.POST)
    if User.objects.filter(email=form['email'].value()):
        return render(request, 'signup/signup.html', {'error':"This login is already in use!"})
    user = UserSerializer(data = request.data)
    if not user.is_valid():
        return render(user.errors, 'signup/signup.html', status=HTTP_400_BAD_REQUEST)
    # user.save()
    # return render(request, 'signup/signup.html', status=HTTP_200_OK)
    
