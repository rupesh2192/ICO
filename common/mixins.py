from django.db import models
from rest_framework.exceptions import APIException


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NoActiveBiddingSession(APIException):
    status_code = 400
    default_detail = 'Bid cannot be placed as there is no ongoing Bidding Session.'
    default_code = 'no_bidding_session'