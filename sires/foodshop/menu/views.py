from django.shortcuts import render, get_object_or_404

from menu.models import category, product


# Create your views here.


menu = ['Продукты', "Бесплатная доставка", "Наш блог", "Органика", "Специальные предложения", "Распродажи"]


def index(request):
    cat = category.objects.all()
    data = {
        'menu': menu,
        'categories': cat,
        'cat_selected': 1,
        'menu_selected': 0,
        'cat_slug': cat[0].slug,
    }
    return render(request, 'menu/index.html', context=data)


def first_page(request, cat_slug):
    cat = category.objects.all()
    categor = get_object_or_404(category, slug=cat_slug)
    data = {
        'menu': menu,
        'categories': cat,
        'cat_selected': categor.pk,
        'menu_selected': 0,
        'cat_slug': cat_slug,
    }
    return render(request, 'menu/index.html', context=data)




