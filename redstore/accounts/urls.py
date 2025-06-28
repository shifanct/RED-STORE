from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name = 'register'),
    path('login/',views.login, name = 'login'),
    path('logout/',views.logout, name = 'logout'),
    path('home_page/',views.home_page, name='home_page')
]