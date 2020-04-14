from django.urls import path
from . import views 

urlpatterns = [
    path('borrow-notes/<int:num>/', views.borrow_notes, name='borrow_notes'),
    path('borrow-com/<int:num>/', views.borrow_com, name='borrow_com'),
    path('borrow-tutor/<int:num>/', views.borrow_tutor, name='borrow_tutor')
]