from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from coin_offering.models import Bid, BidSession
from common.mixins import NoActiveBiddingSession


class BidSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Bid
        fields = ("price", "quantity", "user")
        read_only_fields = ['bid_session', 'user']

    def create(self, validated_data):
        active_session = BidSession.active_session()
        if active_session:
            validated_data['bid_session'] = active_session
        else:
            raise NoActiveBiddingSession()

        return super(BidSerializer, self).create(validated_data)
