from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# from django.http import HttpResponse
from datetime import datetime
from posts.forms import PostForm

from posts.models import Post
# Create your views here.


@login_required
def list_posts(request):

    posts = Post.objects.all().order_by('-created')

    return render(request, 'posts/feed.html', {'posts': posts})


@login_required
def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/create_post.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        })
