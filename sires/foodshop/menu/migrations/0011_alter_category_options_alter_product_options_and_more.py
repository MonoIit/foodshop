# Generated by Django 5.1 on 2024-08-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_delete_blog_delete_blog_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайды'},
        ),
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=0, verbose_name='В наличии'),
        ),
    ]
