# Generated by Django 2.0 on 2019-08-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20190802_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='bank_transaction_id',
            new_name='bank_txnid',
        ),
        migrations.AlterField(
            model_name='payment',
            name='gateway',
            field=models.CharField(choices=[('PAYU', 'Payumoney'), ('PAYTM', 'Paytm')], max_length=5),
        ),
    ]
