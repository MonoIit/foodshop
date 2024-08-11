from django.shortcuts import render

# Create your views here.


def index(request):
    data = {
        'navigation': 1,

    }
    return render(request, 'menu/index.html')