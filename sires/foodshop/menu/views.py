from django.shortcuts import render, get_object_or_404

from menu.models import category, product, blog, slide



# Create your views here.


menu = ['Продукты', "Бесплатная доставка", "Наш блог", "Органика", "Специальные предложения", "Распродажи"]


def show_shop(request):
    blogs = blog.objects.all()
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




