from django.urls import path
from . import views 

urlpatterns = [
    path('return-book/', views.return_book, name='return_book'),
]