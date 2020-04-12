from django.urls import path
from . import views 

urlpatterns = [
    path('math/', views.math, name='math'),
    path('science/', views.science, name='science'),
    path('book/<int:num>/', views.blogbook, name='blogbook'),
    
]