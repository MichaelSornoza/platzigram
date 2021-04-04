from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# EXCEPTIONS
from django.db.utils import IntegrityError

from .models import Profile

# Create your views here.

from users.forms import ProfileForm


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


@login_required
def updated_profile_view(request):

    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']

            profile.save()

            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


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


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
