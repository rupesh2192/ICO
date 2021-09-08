from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from coin_offering.serializers import BidSerializer


class BidViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = BidSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(user=self.request.user)
