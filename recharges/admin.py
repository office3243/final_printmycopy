from django.contrib import admin
from . models import Recharge, CustomPack, OfferPack


class RechargeAdmin(admin.ModelAdmin):

    list_display = ("wallet", "pack", "gateway", "status")
    list_filter = ("gateway", "status", "created_on", "wallet__user")


admin.site.register(Recharge, RechargeAdmin)
admin.site.register(OfferPack)
admin.site.register(CustomPack)

