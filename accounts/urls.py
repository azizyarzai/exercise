from django.urls import path
from accounts.views import register_user, login_user, logout_user

app_name = 'accounts'

urlpatterns = [
    path("register/", register_user, name='register'),
    path("login/", login_user, name='login'),
    path("logout/", logout_user, name='logout'),
]
