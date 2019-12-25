from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from . import views
from .forms import CustomLoginForm
from django.views.generic import TemplateView

app_name = "accounts"

urlpatterns = [

    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'),
        name='login'),

    url(r"^register/$", views.RegisterView.as_view(), name='register'),

    url(r"^profile/$", views.ProfileUpdateView.as_view(), name='profile_update'),

    url(r"^password/change/$", views.password_change, name='password_change'),

    # url(r"^password/change/$", views.PasswordChangeView.as_view(), name='password_change'),

    url(r'^logout/$', logout_then_login, name='logout'),

]
