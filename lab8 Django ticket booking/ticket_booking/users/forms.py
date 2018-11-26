from django import forms

class UserSigninForms(forms.Form):
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(label='password', max_length=100)

class UserSignupForm(forms.Form):
    fname = forms.CharField(label='fname', max_length=100)
    lname = forms.CharField(label='lname', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(label='password', max_length=100)