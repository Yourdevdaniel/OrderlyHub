from django.urls import path, include
from .views import *

urlpatterns = [
    path("api/auth/register/", RegisterView.as_view(), name='register'),
    path("/api/auth/login/", LoginView.as_view(), name='login'),
    path("/api/auth/token/refresh/", TokenRefreshView.as_view(), name='TokenRefresh'),
    path("/api/auth/me/", MeView.as_view(), name='MeView'),
    path("/api/auth/logout/", LogoutView.as_view(), name="Logout")
]