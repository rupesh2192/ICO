import uuid

from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models, transaction
# Create your models here.
from django.utils import timezone

from common.mixins import BaseModel

User = get_user_model()


class Token(BaseModel):
    token_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    assigned_to = models.ForeignKey(User, related_name='assigned_tokens', null=True, default=None, blank=True,
                                    on_delete=models.PROTECT)
    assigned_date = models.DateTimeField(default=None, null=True, blank=True)
    bid = models.ForeignKey('Bid', related_name="allocated_tokens", on_delete=models.PROTECT, default=None, null=True, blank=True)

    class Meta:
        ordering = ('-assigned_date', 'assigned_to')


class BidSession(BaseModel):
    start_time = models.DateTimeField(null=False, blank=False)
    end_time = models.DateTimeField(null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title

    @classmethod
    def active_session(cls):
        try:
            return cls.objects.get(start_time__lte=timezone.now(), end_time__gt=timezone.now())
        except cls.DoesNotExist as e:
            return False

    def allocate(self):
        for bid in self.bids_received.filter(processed=False).order_by('-price', 'created_at'):
            if not bid.allocate():
                break

    @property
    def is_active(self):
        return self.start_time <= timezone.now() <= self.end_time


class Bid(BaseModel):
    user = models.ForeignKey(User, related_name="bids", null=False, blank=False, on_delete=models.CASCADE)
    bid_session = models.ForeignKey(BidSession, related_name="bids_received", null=False, blank=False,
                                    on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(validators=[validators.MinValueValidator(1)], null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    processed = models.BooleanField(default=False)
    allocated_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user}-{self.price}-{self.quantity}-{self.created_at}"

    def allocate(self):
        with transaction.atomic():
            available_tokens = Token.objects.filter(assigned_to=None).order_by("created_at").count()
            # If all tokens already exhausted
            if not available_tokens:
                return False
            # Required tokens are available
            if available_tokens >= self.quantity:
                tokens = Token.objects.filter(assigned_to=None).order_by("created_at")[:self.quantity]

            # Limited tokens are available
            else:
                tokens = Token.objects.filter(assigned_to=None).order_by("created_at")
            self.allocated_quantity = Token.objects.filter(pk__in=tokens).update(assigned_to=self.user, bid=self, assigned_date=timezone.now())
            self.processed = True
            self.save()

        return True
