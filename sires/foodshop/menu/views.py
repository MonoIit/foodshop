from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from menu.models import category, product, slide
from shared_models.models import Blog

menu = (('Продукты', 'shop'), ("Бесплатная доставка", 'delivery'),
        ("Наш блог", 'blogs'), ("Органика", 'organic'), ("Специальные предложения", 'offers'),
        ("Распродажи", 'sales'))


def show_shop(request):
    blogs = Blog.objects.all()
    slides = slide.objects.all()
    cat = category.objects.all()
    goods = product.objects.all()
    data = {
        'menu': menu,
        'categories': cat,
        'cat_selected': 1,
        'menu_selected': 0,
        'blogs': blogs,
        'slides': slides,
        'goods': goods,
    }
    return render(request, 'menu/product_shop.html', context=data)


def products_by_category(request, cat_slug):
    categor = get_object_or_404(category, slug=cat_slug)
    goods = categor.product.all()
    data = {
        'goods': goods,
    }
    return render(request, 'menu/list_products.html', context=data)


def delivery(request):
    return HttpResponse('Бесплатная доставка')


def blogs(request):
    return HttpResponse('blogs')


def organic(request):
    return HttpResponse('organic')


def offers(request):
    return HttpResponse('offers')


def sales(request):
    return HttpResponse('sales')








