from django.urls import path
from django.views.generic import TemplateView


from users import views

urlpatterns = [
    # Posts
    path(
        route='<str:username>/',
        view=TemplateView.as_view(template_name='users/detail'),
        name='detail'
    ),
    # Management
    path(
        route='users/signup',
        view=views.signup_view,
        name='signup'
    ),
    path(
        route='users/login',
        view=views.login_view,
        name='login'
    ),
    path(
        route='users/logout',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='users/me/profile',
        view=views.updated_profile_view,
        name='update_profile'
    )
]
