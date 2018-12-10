"""
Author: Anthony C. Emmanuel
Title: Django Project Starter Template
Version: 1.0.0
Language: Python 3.6
Date: 07-12-2018
License: 3-clause BSD
"""
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, UpdateView)
from user.models import CustomUser
# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    """Logged in user Dashboard"""

    template_name = 'user/home.html'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        """Get authenticated user information."""

        context = super().get_context_data(**kwargs)
        context['logged_user'] = CustomUser.objects.filter(username = self.request.user)

        return context

class Profile(LoginRequiredMixin, UpdateView):
    """View and Update authenticated user profile."""

    model = CustomUser
    fields = ['first_name', 'last_name', 'photo']
    template_name = 'user/profile.html'
    success_url = reverse_lazy('user:profile')

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        """Get authenticated user information."""

        context = super().get_context_data(**kwargs)
        context['logged_user'] = CustomUser.objects.filter(username = self.request.user)

        return context
