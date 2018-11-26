from django.shortcuts import render

def signin(request):
    return render(request, 'signin/signin.html')

def signup(request):
    return render(request, 'signup/signup.html')
