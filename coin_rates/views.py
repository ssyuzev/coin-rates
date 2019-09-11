"""Views for coin_rates app."""

import logging

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _

from .models import CoinPair
from .forms import AddCoinPairForm

logger = logging.getLogger('coin_rates.views')


class HomePageView(TemplateView):
    """Home page view."""

    template_name = 'coin_rates/home.html'

    def get_context_data(self, **kwargs):
        """Add variables to view context."""
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        """View details for HTTP GET method."""
        context = self.get_context_data(**kwargs)
        coun_pairs = CoinPair.objects.all().order_by('created')
        context['coin_pairs'] = coun_pairs
        context['last_update'] = coun_pairs.first().get_last_update().created
        return self.render_to_response(context)


class AddCoinPairView(TemplateView):
    """Add Coin Pair View."""

    template_name = 'coin_rates/add_coin_pair.html'
    form_class = AddCoinPairForm

    def get_context_data(self, **kwargs):
        """Add variables to view context."""
        context = super(AddCoinPairView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        """View details for HTTP GET method."""
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request):
        """View details for HTTP POST method."""
        post_data = request.POST or None
        form = self.form_class(post_data)
        context = self.get_context_data(form=form)
        if post_data is not None:
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        return self.render_to_response(context)

    def form_invalid(self, form, **kwargs):
        """Add some background work if form is invalid."""
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def form_valid(self, form, **kwargs):
        """Add some background work and save the form data."""
        context = self.get_context_data(**kwargs)
        context['form'] = form
        form.save(self.request)
        messages.success(
            self.request, _("Your coin pair added successfully."))
        return redirect('home')
