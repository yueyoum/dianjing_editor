from django.contrib import admin
from apps.auction.models import Auction
# Register your models here.


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'duration', 'tax')

