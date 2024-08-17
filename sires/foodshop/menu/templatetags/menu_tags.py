from django import template
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404

from menu.models import category, product

register = template.Library()


@register.filter
def stars(rating):
    stars_output = []
    for i in range(5):
        if rating >= (i * 2 + 2):
            stars_output.append('2')
        elif rating == (i * 2 + 1):
            stars_output.append('1')
        else:
            stars_output.append('0')
    return "".join(stars_output)



@register.inclusion_tag('menu/list_categories.html')
def show_categories():
    cats = category.objects.all()
    return {'categories': cats}


@register.inclusion_tag('menu/list_products.html')
def show_products(goods):
    return {'goods': goods}


