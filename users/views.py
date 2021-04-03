from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# EXCEPTIONS
from django.db.utils import IntegrityError

from .models import Profile

# Create your views here.


def signup_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password not found'})

        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email
            )

            profile = Profile(user=user)

            user.save()
            profile.save()

            return redirect('login')

        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

    else:
        return render(request, 'users/signup.html')


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    else:
        return render(request, 'users/login.html')


@ login_required
def logout_view(request):
    logout(request)
    return redirect('login')
