# Generated by Django 2.0 on 2019-08-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0002_wallet_free_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='free_balance',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=6),
        ),
    ]
