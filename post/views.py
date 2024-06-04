from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'post/index.html')


def about(request):
    return render(request, 'post/about.html')


def home(request):
    return render(request, 'post/home.html')


def contacts(request):
    return render(request, 'post/contacts.html')




