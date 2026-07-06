import django.utils.timezone
from django.db import models, connection


class Category(models.Model):
    name = models.CharField('наименование', max_length=50)
    description = models.CharField('описание', max_length=150)
    created_at = models.DateField('дата создания', default=django.utils.timezone.now)

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE catalog_category CASCADE')
            cursor.execute('ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Product(models.Model):
    name = models.CharField('наименование', max_length=50)
    description = models.CharField('описание', max_length=150)
    image = models.ImageField('изображение', upload_to='images', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField('цена за штуку', max_digits=10, decimal_places=2)
    created = models.DateField('дата создания', default=django.utils.timezone.now)
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='добавивший', blank=True, null=True)
    is_published = models.BooleanField('опубликован ли', default=False)

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE catalog_product CASCADE')
            cursor.execute('ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Version(models.Model):
    name = models.CharField('наименование', max_length=150)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.FloatField(verbose_name='номер')
    flag = models.BooleanField(verbose_name='признак')

    def __str__(self):
        return f"{self.name} v {self.number}"

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'



class Contact(models.Model):
    name = models.CharField('имя', max_length=30)
    phone = models.CharField('телефон', max_length=12)
    message = models.TextField()

    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = 'обратные связи'
