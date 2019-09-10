"""Forms for coin_rates app."""

from django import forms

from .models import CoinPair


class AddCoinPairForm(forms.ModelForm):
    """Add coin pair form."""

    class Meta:
        """Django magic."""

        model = CoinPair
        fields = ('base', 'target', )

    def clean(self):
        """Override default clean method."""
        cleaned_data = super(AddCoinPairForm, self).clean()
        base = cleaned_data.get('base', '').lower()
        target = cleaned_data.get('target', '').lower()
        coin_pair_exist = CoinPair.objects.filter(
            base=base, target=target).exists()
        cleaned_data['base'] = base
        cleaned_data['target'] = target
        '''If current coin pair already exists then raise error.'''
        if coin_pair_exist:
            raise forms.ValidationError("Current coin pair already exists!")

        return cleaned_data
