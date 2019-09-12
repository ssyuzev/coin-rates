"""Tests for coin_rates app views."""
from django.contrib.auth.models import AnonymousUser
import pytest

from .. import views


pytestmark = pytest.mark.django_db


class TestHomePageView:
    """Test bundle for HomePageView."""

    def test_anonymous(self, rf):
        """Access denied for unsigned in users."""
        req = rf.get('/')
        req.user = AnonymousUser()
        req.session = {}
        resp = views.HomePageView.as_view()(req)
        assert resp.status_code == 200, ("Should show home page")
