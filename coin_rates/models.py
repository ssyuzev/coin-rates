"""Models for coin_rates app."""

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel


class CoinPair(TimeStampedModel):
    """Model for coin pairs."""

    base = models.CharField(_("Base"), max_length=3, default='')
    target = models.CharField(_("Target"), max_length=3, default='')

    class Meta:
        """Django magic."""

        verbose_name_plural = "Coin Pairs"

    def __str__(self):
        """Model string representation."""
        return "{}-{}".format(self.base.lower(), self.target.lower())

    def get_last_update(self):
        """Get coin pair's last update values."""
        return self.ticker.all().order_by('-created').first()


class CoinPairTicker(TimeStampedModel):
    """Model for coin pairs ticker."""

    coin_pair = models.ForeignKey(
        CoinPair, on_delete=models.CASCADE, null=True,
        related_name='ticker',
    )
    price = models.CharField(max_length=24, blank=True, default='')
    volume = models.CharField(max_length=24, blank=True, default='')
    change = models.CharField(max_length=24, blank=True, default='')

    def __str__(self):
        """Model string representation."""
        return "{} at {}".format(self.coin_pair, self.created)
