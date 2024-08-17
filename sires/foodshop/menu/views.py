import sys
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from menu.models import category, product, slide
from blogs.models import Blog
from foodshop.utils import search_products

menu = (('Продукты', 'shop'), ("Бесплатная доставка", 'delivery'),
        ("Наш блог", 'blog'), ("Органика", 'organic'), ("Специальные предложения", 'offers'),
        ("Распродажи", 'sales'))


def show_shop(request):
    blogs = Blog.objects.all()
    slides = slide.objects.all()
    cat = category.objects.all()
    goods = product.objects.filter(in_stock=True).order_by('name')
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
    goods = categor.product.filter(in_stock=True).order_by('name')
    data = {
        'goods': goods,
    }
    return render(request, 'menu/list_products.html', context=data)


def show_found_products(request):
    query = request.GET.get('q', '')
    if query:
        product_ids = search_products(query)
        products = product.objects.filter(id__in=product_ids)
    else:
        products = product.objects.none()

    return render(request, 'menu/search_result.html', context={'products': products})

def delivery(request):
    return HttpResponse('Бесплатная доставка')


def organic(request):
    return HttpResponse('organic')


def offers(request):
    return HttpResponse('offers')


def sales(request):
    return HttpResponse('sales')








