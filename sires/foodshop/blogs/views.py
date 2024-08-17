from django.http import HttpResponse
from django.shortcuts import render


menu = (('Продукты', 'shop'), ("Бесплатная доставка", 'delivery'),
        ("Наш блог", 'blog'), ("Органика", 'organic'), ("Специальные предложения", 'offers'),
        ("Распродажи", 'sales'))


def blog(request):
    data = {
        'menu': menu,
        'menu_selected': 2,
    }
    return render(request, 'blogs/index.html', context=data)