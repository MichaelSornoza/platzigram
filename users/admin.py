from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import Profile

# Register your models here.

# admin.site.register(Profile)


class ExporCsvMixin:
    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        meta = self.model._meta

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)
        writer.writerow(
            [
                'email',
                'first_name',
                'last_name',
                'phone_number'
            ]
        )

        return response


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin, ExporCsvMixin):

    list_display = (
        'pk',
        'user',
        'phone_number',
        'website',
        'picture'
    )
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    """
        (
            'NOMBRE SECTION', {
                'fields': (
                    ('field que se quiere')
                )
            }
        )
    
    """

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            ),
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography'),
            ),
        }),
        ('Metadata', {
            'fields': (('created', 'modified'))
        })
    )

    readonly_fields = ('created', 'modified')

    actions = ['export_as_csv']


class ProfileInline(admin.StackedInline):

    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'


class UserAdmin(BaseUserAdmin):

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
