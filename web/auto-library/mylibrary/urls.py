from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.auth_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.my_logout, name='my_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]