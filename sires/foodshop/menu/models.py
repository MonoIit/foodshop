import json

from django.db import models
from django.urls import reverse
from firewind.core import firewind


class product(models.Model):
    name = models.CharField(max_length=75, verbose_name="Название продукта")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    category = models.ForeignKey(to='category', related_name='product', on_delete=models.DO_NOTHING)
    cost = models.FloatField(verbose_name="Цена")
    sale = models.FloatField(default=0, verbose_name="Скидка в процентах")
    image = models.ImageField(upload_to='photos/')
    stars = models.IntegerField(verbose_name="Оценка")
    reviews = models.IntegerField(verbose_name="Количество отзывов", default=0)
    in_stock = models.BooleanField(verbose_name="В наличии", default=0)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def save(self, *args, **kwargs):
        """
        Переопределяем логику сохранения объекта в БД
        После сохранения в таблицу product берётся поле description и ищется его индекс,
        затем этот индекс сохраняется в таблицу ProductDescription
        """
        # Сначала сохраняем объект Product
        super().save(*args, **kwargs)
        analyzer = firewind()

        # После сохранения создаем индекс для продукта
        index_data = analyzer.make_index(self.description)

        # Кодируем в json
        index_data['words'] = [node.to_dict() for node in index_data['words']]

        # Создаём или обновляем объект в БД
        ProductDescription.objects.update_or_create(fid=self, defaults={'index': index_data})

class category(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название категории")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    icon = models.ImageField(upload_to='icons/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_by_category', kwargs={'cat_slug': self.slug})



    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class slide(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Контент")
    button_name = models.CharField(max_length=50, verbose_name="Заголовок кнопки перехода")
    image = models.ImageField(upload_to='slides/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"


class ProductDescription(models.Model):
    fid = models.OneToOneField(product, on_delete=models.CASCADE)
    index = models.JSONField(null=True)

    def __str__(self):
        return f'Index for {self.fid.name}'


