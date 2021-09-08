from django.core.management.base import BaseCommand, CommandError
from coin_offering.models import BidSession, Token, Bid


class Command(BaseCommand):
    help = 'Resets allocation of all tokens'

    def handle(self, *args, **options):
        Token.objects.update(assigned_to=None, assigned_date=None)
        Bid.objects.update(processed=False, allocated_quantity=0)
