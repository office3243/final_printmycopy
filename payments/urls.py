from django.conf.urls import url
from . import views
from . import paytm_views

app_name = 'payments'

urlpatterns = [

    url(r'^paytm/create_payment/$', paytm_views.create_payment, name='paytm_create_payment'),
    url(r'^paytm/response/$', paytm_views.response, name='paytm_response'),

]
