from django.urls import path
from . import views 

urlpatterns = [
    path('borrow-notes', views.borrow_notes, name='borrow_notes')
]