from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):

    list_display = ("recharge", "amount", "gateway", "status")
    list_filter = ("gateway", "status", "created_on", "recharge__wallet__user")

admin.site.register(Payment, PaymentAdmin)
