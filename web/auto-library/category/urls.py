from django.urls import path
from . import views 

urlpatterns = [
    path('category/', views.category, name='category'),
    path('book/', views.blogbook, name='blogbook'),
    
]