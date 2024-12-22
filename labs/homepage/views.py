from django.shortcuts import render


# Create your views here.
def showBooks(request):
    template = 'homepage/homepage.html'
    return render(request, template, {})