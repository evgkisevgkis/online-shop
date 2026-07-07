from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Команда для добавления группы для модераторов каталога'
    def handle(self, *args, **options):
        group = Group.objects.create(name='Blog_Managers')
        perm = Permission.objects.get(
            content_type__app_label='blog',
            codename='change_article'
        )
        group.permissions.add(perm)
