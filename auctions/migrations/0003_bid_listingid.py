# Generated by Django 3.1 on 2020-09-21 18:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_remove_bid_listingid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='listingid',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]