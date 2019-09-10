"""Coin rates models for Admin Area."""

from django.contrib import admin

from .models import CoinPair, CoinPairTicker


@admin.register(CoinPair)
class CoinPairAdmin(admin.ModelAdmin):
    """CoinPair model in Admin Area."""

    list_display = ('__str__', 'base', 'target', 'created', 'modified')


@admin.register(CoinPairTicker)
class CoinPairTickerAdmin(admin.ModelAdmin):
    """CoinPairTicker model in Admin Area."""

    list_display = (
        'coin_pair', 'price', 'volume', 'change', 'created', 'modified')
