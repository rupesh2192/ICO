from django.contrib import admin, messages

# Register your models here.
from django.contrib.admin import ModelAdmin
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import re_path, reverse

from coin_offering.models import BidSession, Bid, Token
from common.enums import Message


@admin.register(BidSession)
class BidSessionAdmin(ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'is_active')
    change_form_template = 'coin_offering/bid_session_change_form.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            re_path(
                r'^allocate/(?P<object_id>.+)$',
                self.allocate_tokens,
                name='allocate-tokens',
            ),
            re_path(
                r'^allocation_report/(?P<object_id>.+)$',
                self.allocation_report,
                name='allocation-report',
            ),
        ]
        return my_urls + urls

    def allocation_report(self, request, object_id=None, *args, **kwargs):
        bids = Bid.objects.filter(bid_session_id=object_id).annotate(
            pending_quantity=F('quantity') - F('allocated_quantity'))
        return render(request, 'coin_offering/allocation_report.html',
                      {'bids': bids, 'bid_session': bids.first().bid_session})

    def allocate_tokens(self, request, object_id=None, *args, **kwargs):
        instance = BidSession.objects.get(pk=object_id)
        if instance.is_active:
            self.message_user(request, Message.BID_SESSION_ACTIVE_ERROR, level=messages.ERROR)

        else:
            instance.allocate()
            self.message_user(request, Message.BID_SESSION_ALLOCATE_SUCCESS, level=messages.SUCCESS)
        return HttpResponseRedirect(
            reverse("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.model_name),
                    args=(object_id,)))


@admin.register(Bid)
class BidModelAdmin(ModelAdmin):
    list_display = ('user', 'quantity', 'price', 'processed', 'allocated_quantity')
    list_filter = ('bid_session',)


@admin.register(Token)
class TokenModelAdmin(ModelAdmin):
    list_display = ('token_id', 'assigned_to', 'assigned_date')
    list_filter = ('assigned_to',)
