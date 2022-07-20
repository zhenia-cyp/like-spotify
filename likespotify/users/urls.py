from django.urls import path

from users.views import RegistrationView,AuthorizationPageView,LoginUserView,ProfilePageView


urlpatterns = [
    path("registration/", RegistrationView.as_view(), name='reg'),
    path("authorizpage/", AuthorizationPageView.as_view(), name='authorizpage'),
    path("profile/", ProfilePageView.as_view(), name='profile'),
    path("login/", LoginUserView.as_view(), ),
]