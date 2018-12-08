from django.shortcuts import render, redirect

def checkSession(request):
    try:
        if request.session['user']:
            print("-- USER Session is not empty --")
            return False
    except:
        print("-- USER Session is empty --")
        return True

def signin(request):
    if not checkSession(request):
        return redirect("/films/")
    return render(request, 'signin/signin.html')

def signup(request):
    if not checkSession(request):
        return redirect("/films/")
    return render(request, 'signup/signup.html')

def logout(request):
    del request.session['user']
    return redirect("/auth/")
