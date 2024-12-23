from django.shortcuts import render
from django.http import JsonResponse
from .models import Books
from django.contrib.auth.models import User


# Create your views here.
def showBooks(request):
    template = 'homepage/homepage.html'

    books = Books.objects.all().order_by('-id')[:10]
    users = User.objects.all()

    return render(request, template, {
        'books': books,
        'users': users
    })


def get_books(request):
    user_id = request.GET.get('user_id', None)
    
    if user_id:
        books = Books.objects.filter(user_id=user_id).values('id', 'title', 'author', 'score', 'description', 'user__username').order_by('-id')
    else:
        books = Books.objects.all().values('id', 'title', 'author', 'score', 'description', 'user__username').order_by('-id')[:10]
    
    return JsonResponse({'books': list(books)})