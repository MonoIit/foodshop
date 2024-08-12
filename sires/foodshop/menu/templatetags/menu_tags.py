from django import template
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404

from menu.models import category, product

register = template.Library()


@register.inclusion_tag('menu/list_categories.html')
def show_categories(cat_selected = 0):
    cats = category.objects.all()
    return {'categories': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('menu/list_products.html')
def show_products(cat_slug):
    cat = get_object_or_404(category, slug=cat_slug)
    products = cat.product.all()
    return {'goods': products}