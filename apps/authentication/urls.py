from django.contrib.auth.views import LoginView

from .views import SignupView, VerifyEmail, SigninView
from django.urls import path

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("signin/", SigninView.as_view(), name="signin"),
    path("email_verify/", VerifyEmail.as_view(), name="email_verify"),
]
