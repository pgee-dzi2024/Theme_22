from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def second(request):
    lst = [1, 2, 3, 4, 5,]
    context = {
        'var1': 'here we put var1',
        'var2': lst,
    }
    return render(request, 'main/second.html', context)
