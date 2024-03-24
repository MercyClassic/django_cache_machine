from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create default superuser'

    def handle(self, *args: tuple, **options: dict) -> None:
        if not User.objects.filter(username='root', email='root@mail.com').exists():
            User.objects.create_superuser(
                username='root',
                email='root@mail.com',
                password='root',
            )
