from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Контент")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    image = models.ImageField(upload_to="blogs/", blank=True)
    category = models.ForeignKey(to='Category', on_delete=models.DO_NOTHING, related_name='blog')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название  категории")
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name
