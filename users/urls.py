from django.urls import path
from django.views.generic import TemplateView


from users import views

urlpatterns = [
    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    # Management
    path(
        route='signup',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='login',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='me/profile',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'
    )
]
