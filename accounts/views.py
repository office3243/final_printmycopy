import requests
from .forms import RegisterForm, ProfileUpdateForm #, PasswordResetForm, PasswordResetNewForm, OTPForm
from django.views.generic import TemplateView, ListView, FormView, View, DetailView, UpdateView
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import alert_messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from .models import User
from django.shortcuts import get_object_or_404


USER_MODEL = User
API_KEY_2FA = settings.API_KEY_2FA

registeration_otp_template = "Registration_Template"

password_reset_otp_template = "Password_Reset_Template"


def send_otp_2fa(request, phone, purpose):
    otp_template = registeration_otp_template if purpose==1 else password_reset_otp_template
    if 'user_session_data' in request.session:
        del request.session['user_session_data']
    url = "http://2factor.in/API/V1/{API_KEY_2FA}/SMS/{phone}/AUTOGEN/{otp_template}".format(API_KEY_2FA=API_KEY_2FA,
                                                                                      phone=phone, otp_template=otp_template)
    response = requests.request("GET", url)
    data = response.json()
    request.session['user_session_data'] = data['Details']
    return True


def otp_generate(request, user):
    request.session["user_session_uuid"] = str(user.uuid)
    send_otp_2fa(request, user.phone, purpose=1)
    messages.info(request, alert_messages.REGISTERATION_OTP_SENT_MESSAGE)
    return redirect("accounts:otp_verify")


def otp_resend(request):
    try:
        user = get_object_or_404(USER_MODEL, uuid=request.session.get('user_session_uuid'))
        return otp_generate(request, user=user)
    except USER_MODEL.DoesNotExist:
        raise Http404("Bad Request")


def check_otp_2fa(otp, otp_session_data):
    url = "http://2factor.in/API/V1/{0}/SMS/VERIFY/{1}/{2}".format(API_KEY_2FA,
                                                                   otp_session_data, otp)
    response = requests.request("GET", url)
    data = response.json()
    return data['Status'] == "Success"


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "accounts/register.html"

    def form_valid(self, form):
        print(form)
        new_user = form.save()
        return otp_generate(self.request, user=new_user)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    form_class = ProfileUpdateForm
    template_name = "accounts/profile_update.html"
    model = USER_MODEL
    success_url = reverse_lazy("accounts:profile_update")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, alert_messages.PROFILE_UPDATED_MESSAGE)
        return super().form_valid(form)


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, alert_messages.PASSWORD_CHANGED_SUCCESS_MESSAGE)
            return redirect('portal:home')
        else:
            messages.error(request, alert_messages.FORM_INVALID_MESSAGE)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form
    })

#
# class PasswordChangeView(LoginRequiredMixin, FormView):
#     form_class = PasswordChangeForm
#     template_name = "accounts/password_change.html"
#
#
#     def form_valid(self, form):
#         user = form.save()
#         update_session_auth_hash(self.request, user)  # Important!
#         messages.success(self.request, alert_messages.PASSWORD_CHANGED_SUCCESS_MESSAGE)
#         return redirect('portal:home')
