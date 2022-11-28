from django.urls import path
from .views import RegisterView, RegisterMentorView, VerifyEmail, LoginApiView, PasswordTokenCheckAPI, RequestPasswordResetEmail, SetNewPasswordAPIView, LogoutAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register_mentor/', RegisterMentorView.as_view(), name='register_mentor'),
    path('verify_email/', VerifyEmail.as_view(), name='verify_email'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
]