from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from mylibrary.models import *
from .forms import *

# Create your views here.
def borrow_book(request,num):
    book = Book_info.objects.get(pk=num)
    borrow_form = BorrowNotesForm()
    return render(request, 'borrow.html', context={
        'form': borrow_form,
        'book': book
    })

@login_required
def borrow_com(request, num):
    computer_id = Computer.objects.get(pk=num)
    user = request.user
    if request.method == 'POST':
        form = BorrowComForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            expire_date = form.cleaned_data['expire_date']            
            post = Borrower_Computer(
                computer = computer_id, 
                borrow_user = user,
                date = date,
                expire_date = expire_date
            )
            post.save()
            computer_id.status_com = 'UNAVAILABLE'
            print("+++++++++++++++++++++++++++++", computer_id.status_com, "testttttttttttttttt")
            computer_id.save()
            messages.success(request, 'Computer Booking is complete :)')
            return redirect('computer')
    borrow_form = BorrowComForm()
    return render(request, 'borrow-com.html', context={
        'form': borrow_form,
        'computer': computer_id
    })

def borrow_tutor(request, num):
    tutorroom = Tutor_room.objects.get(pk=num)
    borrow_form = BorrowTutorForm()
    print(tutorroom)
    return render(request, 'borrow-tutor.html', context={
        'form': borrow_form,
        'tutorroom':  tutorroom
    })
