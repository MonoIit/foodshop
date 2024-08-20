from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'user'

urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
]
