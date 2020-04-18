
from .forms import *
from django.shortcuts import render, redirect

# Create your views here.
def return_book(request,num):
    returnbook = Borrow_Notes.objects.get(pk=num)
    return_form = ReturnBookForm()
    datenow = datetime.now().date()
    datereturn = returnbook.return_date.date()
    user = request.user
    Diff = (datenow - datereturn)
    count = (Diff.days*10)
    postreturn = CalculateFines.objects.filter(borrow_user=returnbook)
    
    if count > 0:
        if len(postreturn) == 0:
            postreturn = CalculateFines(date=datenow,  borrow_user=returnbook, user_id=user, charg=count)
            postreturn.save()

        get_return = return_book_last1(request, user, returnbook)
        context = {
            'get_return' : get_return
        }
        print(context)
        return render(request, 'return-book.html', context=context)
    else:
        returnbook.delete()
        return redirect('dashboard')

def return_book_last1(request, usert, returnbook):
    calculate = CalculateFines.objects.filter(borrow_user=returnbook)
    return calculate

