from django.core.management.base import BaseCommand, CommandError
from coin_offering.models import BidSession


class Command(BaseCommand):
    help = 'Allocates tokens for given bidding session'

    def add_arguments(self, parser):
        parser.add_argument('bid_session_id', type=int)

    def handle(self, *args, **options):
        bid_session = BidSession.objects.get(id=options['bid_session_id'])
        bid_session.allocate()
        self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % bid_session))