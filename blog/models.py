import django.utils.timezone
from django.db import models

class Article(models.Model):
    name = models.CharField('заголовок', max_length=50)
    slug = models.CharField('slug', max_length=150, null=True, blank=True)
    content = models.TextField('содержимое')
    image = models.ImageField('превью', upload_to='images', blank=True, null=True)
    date_created = models.DateField('дата создания', default=django.utils.timezone.now)
    is_published = models.BooleanField('опубликовано', default=True)
    views_count = models.IntegerField('количество просмотров', default=0)
