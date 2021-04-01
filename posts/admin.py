from django.contrib import admin

from .models import Post

# Register your models here.


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'user',
        'profile',
        'tittle',
        'photo',
        'created',
        'modified'
    ]

    list_display_links = [
        'pk',
        'user'
    ]

    list_editable = (
        'tittle',
        'photo'
    )

    search_fields = (
        'user__username',
        'tittle',
        'pk'
    )

    list_filter = (
        'created',
        'modified',
        'tittle'
    )

    filter_fields = (
        'created',
        'modified',
        'tittle'
    )
