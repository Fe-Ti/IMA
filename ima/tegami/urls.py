from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'tegami'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/form', views.index, name='register_form'),
    path('registration/register', views.index, name='register'),
    path('profile/', views.profile, name='profile'),
    path('chats/<int:chat_id>/', views.chat, name='chat'),
    path('chats/<int:chat_id>/send', views.send, name='send'),
    path('accounts/profile/', views.accprofile, name='accprofile'),
    path('login/', auth_views.LoginView.as_view(template_name='tegami/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='tegami/logged_out.html'), name='logout'),
    ]

