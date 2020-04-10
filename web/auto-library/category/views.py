from django.shortcuts import render

# Create your views here.
def category(request):
    return render (request, 'category/index.html')

def blogbook(request):
    return render (request, 'category/book.html')



