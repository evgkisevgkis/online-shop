from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Команда для добавления группы для модераторов каталога'
    def handle(self, *args, **options):
        group = Group.objects.create(name='Catalog_Moderators')
        perm = Permission.objects.get(
            content_type__app_label='catalog',
            codename='change_product'
        )
        group.permissions.add(perm)
