#imports
from django.urls import path
from .views import RegisterView, SetNewPasswordAPIView, ChangePasswordView, VerifyEmail, LoginAPIView, \
    PasswordTokenCheckAPI, RequestPasswordResetEmail, UserListAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
#url patterns
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('users/<int:pk>/', UserListAPIView.as_view(), name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/', 
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
         path('change-password/', ChangePasswordView.as_view(), name='change-password')
]

