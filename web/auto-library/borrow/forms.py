from datetime import datetime, timedelta
from django import forms
from django.forms import ModelForm, TextInput, Select
from mylibrary.models import *
from django.contrib.auth.models import User


class BorrowNotesForm(forms.Form):
    # book_isbn = forms.ModelChoiceField(queryset=Book_info.objects.all(), widget=forms.TextInput(attrs={
    #     'class': 'form-control', 
    #     'readonly':'readonly'
    #     }))

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

class BorrowComForm(forms.ModelForm):
    class Meta:
        model = Borrower_Computer
        fields = ('computer', 'date', 'borrow_user')
        widgets = {
            'computer': Select(attrs={'class': 'form-control mb-5'}),
            'date': TextInput(attrs={'class': 'form-control mb-5', 'readonly': 'readonly'}),
            'borrow_user': Select(attrs={'class': 'form-control mb-5'}),
        }
        labels = {
        "computer": "COMPUTER",
        "date": "DATE",
        "borrow_user": "USER",
    }


class BorrowTutorForm(forms.Form):
    date = forms.DateField(initial=datetime.now(), widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'readonly':'readonly'
        }))
    tutor_room = forms.ModelChoiceField(queryset=Tutor_room.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
        }))
    borrow_user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
        }))