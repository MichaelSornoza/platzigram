from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        """ FORM SETTINGS """
        model = Post
        fields = ('user', 'profile', 'tittle', 'photo')
