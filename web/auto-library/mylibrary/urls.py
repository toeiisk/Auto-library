from django.urls import path
from django.conf.urls import url, include
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.auth_login, name='login'),
    path('logout/', views.my_logout, name='my_logout'),
    path('borrowed/<int:num>/', views.borrowed, name='borrowed'),
    path('dashboard/', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register,name='register'),
    # url(r'^check_login/$', views.check_login, name='check_login'),
]