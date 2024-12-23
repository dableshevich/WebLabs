from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from homepage.models import Books

from django.contrib.auth import authenticate, login


# Create your views here.
def register(request):
    template = 'users/register.html'

    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.password = make_password(password)
        else:
            user = User.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    password=make_password(password)
                )

        user.save()

        return redirect('login')

    return render(request, template, {})


def user_login(request):
    template = 'users/login.html'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            remember_me = request.POST.get('remember_me')
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('homepage')

    return render(request, template, {})


def add_new_book(request):
    template = 'users/add_new_book.html'
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        score = request.POST['score']
        description = request.POST['description']

        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
        else:
            user = None
        
        book = Books(
            title=title,
            author=author,
            score=score,
            user=user,
            description=description
        )

        book.save()

        return redirect('/')

    return render(request, template, {})


def get_user_books(request, id):
    template = 'users/get_user_books.html'

    user = User.objects.get(id=id)
    books = Books.objects.all().filter(user=user).order_by('-id')

    return render(request, template, {
        'username': user.username,
        'books': books
    })