# Generated by Django 2.2.5 on 2019-09-10 11:19

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoinPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('base', models.CharField(default='', max_length=3, verbose_name='Base')),
                ('target', models.CharField(default='', max_length=3, verbose_name='Target')),
            ],
            options={
                'verbose_name_plural': 'Coin Pairs',
            },
        ),
        migrations.CreateModel(
            name='CoinPairTicker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('price', models.CharField(blank=True, default='', max_length=24)),
                ('volume', models.CharField(blank=True, default='', max_length=24)),
                ('change', models.CharField(blank=True, default='', max_length=24)),
                ('coin_pair', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticker', to='coin_rates.CoinPair')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
