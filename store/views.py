from django.shortcuts import render


def index(request):
    return render(request, 'store/index.html')


def shop(request):
    return render(request, 'store/shop.html')


def about(request):
    return render(request, 'store/about.html')


def contact(request):
    return render(request, 'store/contact.html')

# Create your views here.
