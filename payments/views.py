from django.contrib.auth.decorators import login_required
from . import paytm_views
from django.http import Http404


@login_required
def create_payment(request, recharge):
    print(recharge.gateway)
    return paytm_views.create_payment(request, recharge)


