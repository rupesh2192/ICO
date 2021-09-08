from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class Message(TextChoices):
    BID_SESSION_ACTIVE_ERROR = _('Cannot allocate tokens for active bidding session, please try after session ends')
    BID_SESSION_ALLOCATE_SUCCESS = _('Bids under the bid session were allocated successfully')