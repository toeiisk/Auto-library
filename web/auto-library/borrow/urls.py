from django.urls import path
from . import views 

urlpatterns = [
    path('borrow-notes', views.borrow_notes, name='borrow_notes'),
    path('borrow-com', views.borrow_com, name='borrow_com')
]