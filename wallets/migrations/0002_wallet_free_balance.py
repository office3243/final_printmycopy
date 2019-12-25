# Generated by Django 2.0 on 2019-07-31 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='free_balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
