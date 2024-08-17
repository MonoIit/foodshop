from django.contrib import admin
from .models import product, category, slide


admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Продуктовый магазин"


@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'cost', 'sale', 'stars', 'reviews')
    list_display_links = ('id', 'name')
    ordering = ['category', 'name']


@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')