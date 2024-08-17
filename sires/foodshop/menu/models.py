from django.db import models
from django.urls import reverse


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
    keywords = models.TextField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

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
    fid = models.ForeignKey(to='product', related_name='description', on_delete=models.DO_NOTHING)
    description = models.TextField()
    index = models.TextField(null=True)
