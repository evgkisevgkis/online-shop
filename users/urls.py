from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from django.urls import path
from users.views import RegisterView, ProfileView, generate_new_password, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path("register", RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('genpassword', generate_new_password, name='generate_new_password'),
    path('verification', email_verification, name='email_verification'),
]
