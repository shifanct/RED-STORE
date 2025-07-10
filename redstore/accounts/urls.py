from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name = 'register'),
    path('login/',views.login, name = 'login'),
    path('logout/',views.logout, name = 'logout'),
    path('',views.home_page, name='home_page'),
    path('reset_password/',views.reset_password, name ='reset_password'),
    path('confirm_password/<user_id>',views.confirm_password,name = 'confirm_password')
]