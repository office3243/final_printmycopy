from django.db import models


class PaymentManager(models.Manager):

    def initiate_payment(self, **kwargs):
        payment = self.create(**kwargs)
        return payment

    def search_payment_payu(self, txnid, amount):

        try:
            payment = self.get_queryset().get(txnid=txnid, amount=amount)
        except:
            payment = None
        return payment

    def search_payment_paytm(self, order_id, amount):
        try:
            payment = self.get_queryset().get(order_id=order_id, amount=amount)
        except:
            payment = None
        return payment

