from django.core.management import BaseCommand
from catalog.models import Category, Product
import os


class Command(BaseCommand):
    help = 'Команда для очистки таблиц и заполнения данными из фикстуры'
    def handle(self, *args, **options):
        Category.truncate()
        Product.truncate()
        os.system('python manage.py loaddata catalog_data.json')