
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
# this render function will render the html file.
def index(request):
    template = 'index.html'
    return render(request, template)


def signup(request):
    signup_template = 'signup.html'
    signin_template = 'signin.html'
    if request.POST:
        data = request.POST
        user = User.objects.filter(email=data.get("email"))
        if user:
            return render(request, signin_template)
        else:
            user = User.objects.create_user(
                first_name=data.get("firstname"),
                last_name=data.get("lastname"),
                username=data.get("email"),
                email=data.get("email"),
                password=data.get("password")
            )
            user.save()
            return render(request, signin_template)
    else:
        return render(request, signup_template)


def signin(request):
    signin_template = 'signin.html'
    if request.POST:
        data = request.POST
        user = authenticate(username=data.get("email"), password=data.get("password"))
        if user:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Successfully Login.')
            return redirect('/home')
        else:
            messages.add_message(request, messages.ERROR, 'Username or Password Incorrect.')
            return redirect('/signin')
    else:
        return render(request, signin_template)


@login_required
def logout_view(request):
    logout(request)
    return redirect("/")

def contact(request):
    return render(request, 'contact.html')

