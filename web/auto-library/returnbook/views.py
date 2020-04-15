
from .forms import *
from django.shortcuts import render, redirect

# Create your views here.
def return_book(request,num):
    returnbook = Borrow_Notes.objects.get(pk=num)
    return_form = ReturnBookForm()
    datenow = datetime.now()
    user = request.user
    postreturn = CalculateFines(date=datenow,  borrow_user=returnbook, user_id=user)
    postreturn.save()
    return redirect('return_book_last')

def return_book_last(request):
    user = request.user.id
    book = Borrow_Notes.objects.get(borrow_user=user)
    # borrow_note = Borrow_Notes.objects.get(borrow_user)
    calculate = CalculateFines.objects.all()
    print(book, '---------->', calculate)
    return render(request, 'return-book.html')
    