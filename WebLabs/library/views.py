from django.shortcuts import render, redirect
from django.template import loader
from django.utils import translation

from .models import LibraryBooks


# Create your views here.
def books_list(request):
    user_language = request.session.get(translation.LANGUAGE_SESSION_KEY, 'ru')
    translation.activate(user_language)

    author = request.GET.get('author')
    title = request.GET.get('title')

    template = 'index.html'
    
    if author and title:
        books = LibraryBooks.objects.raw(f"SELECT * FROM library_books WHERE author LIKE '%{author}%' AND title LIKE '%{title}%'")
    elif author:
        books = LibraryBooks.objects.raw(f"SELECT * FROM library_books WHERE author LIKE '%{author}%'")
    elif title:
        books = LibraryBooks.objects.raw(f"SELECT * FROM library_books WHERE title LIKE '%{title}%'")
    else:
        books = LibraryBooks.objects.all()

    return render(request, template, {'books': books})


def books_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')

        LibraryBooks.objects.create(
            title=title,
            author=author
        )
    
        return redirect('/')
    else:
        return books_list(request)
