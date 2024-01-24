from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def second(request):
    return render(request, 'main/second.html')
