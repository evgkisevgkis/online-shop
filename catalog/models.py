from django.db import models


class Product(models.Model):
    name = models.CharField('наименование', max_length=50)
    description = models.CharField('описание', max_length=150)
    image = models.ImageField('изображение', upload_to='images', blank=True, null=True)
    category = models.CharField('категория', max_length=50)
    price = models.DecimalField('цена за штуку', max_digits=10, decimal_places=2)
    created = models.DateField('дата создания')
    changed = models.DateField('дата последнего изменения')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Category(models.Model):
    name = models.CharField('наименование', max_length=50)
    description = models.CharField('описание', max_length=150)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
