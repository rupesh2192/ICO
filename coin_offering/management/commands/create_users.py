from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from coin_offering.models import BidSession, Token, Bid


class Command(BaseCommand):
    help = 'Create Initial Users'

    def handle(self, *args, **options):
        try:
            User = get_user_model()
            User.objects.create_superuser('admin', 'admin@ico.com', 'admin')
            User.objects.create_user('john', 'john@ico.com', 'admin')
            User.objects.create_user('mike', 'mike@ico.com', 'admin')
        except: pass

