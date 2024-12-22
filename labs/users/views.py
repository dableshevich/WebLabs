from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from django.contrib.auth import authenticate, login


# Create your views here.
def register(request):
    template = 'users/register.html'

    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['username']
        password = request.POST['password']

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