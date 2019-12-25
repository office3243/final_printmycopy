from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, View


class HomeView(LoginRequiredMixin, TemplateView):

    template_name = "portal/home.html"