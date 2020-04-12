from datetime import datetime, timedelta
from django import forms
from django.forms import ModelForm
from mylibrary.models import *


class BorrowNotesForm(forms.Form):
    book_isbn = forms.ModelChoiceField(queryset=Book_info.objects.all(), widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'readonly':'readonly'
        }))
    date = forms.DateField(initial=datetime.now(), widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'readonly':'readonly'
        }))
    return_date = forms.DateTimeField(initial=datetime.now()+timedelta(days=7), widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'readonly':'readonly'
        }))
    borrow_user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
        }))

class BorrowComForm(forms.Form):
    date = forms.DateField(initial=datetime.now(), widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'readonly':'readonly'
        }))
    computer = forms.ModelChoiceField(queryset=Computer.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
        }))
    borrow_user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
        }))