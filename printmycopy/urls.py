from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r"^", include("portal.urls", namespace="portal")),
    url(r"^accounts/", include("accounts.urls", namespace="accounts")),
    url(r"^complaints/", include("complaints.urls", namespace="complaints")),
    url(r'^wallets/', include('wallets.urls', namespace='wallets')),
    url(r'^payments/', include('payments.urls', namespace='payments')),
    url(r'^recharges/', include('recharges.urls', namespace='recharges')),
]

if settings.DEBUG:
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
