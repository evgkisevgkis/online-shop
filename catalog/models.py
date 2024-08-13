from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование'),
    description = models.CharField(max_length=150, verbose_name='описание'),
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='изображение')
    category = models.CharField(max_length=50, verbose_name='категория'),
    price = models.DecimalField(max_length=15, verbose_name='цена за штуку'),
    created = models.DateField(verbose_name='дата создания'),
    changed = models.DateField(verbose_name='дата последнего изменения')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
