from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.models import User
# EXCEPTIONS
from django.db.utils import IntegrityError

from .models import Profile

from posts.models import Post
# Create your views here.

from users.forms import ProfileForm, SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


# @login_required
# def updated_profile_view(request):

#     profile = request.user.profile

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)

#         if form.is_valid():
#             data = form.cleaned_data

#             profile.website = data['website']
#             profile.biography = data['biography']
#             profile.phone_number = data['phone_number']
#             profile.picture = data['picture']

#             profile.save()

#             url = reverse('users:detail', kwargs={
#                           'username': request.user.username})

#             return redirect(url)
#     else:
#         form = ProfileForm()

#     return render(
#         request=request,
#         template_name='users/update_profile.html',
#         context={
#             'profile': profile,
#             'user': request.user,
#             'form': form
#         }
#     )


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    else:
        return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')
