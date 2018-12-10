"""
Author: Anthony C. Emmanuel
Title: Django Project Starter Template
Version: 1.0.0
Language: Python 3.6
Date: 07-12-2018
License: 3-clause BSD
"""

from django.conf.urls import url
from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('profile/', views.Profile.as_view(), name='profile'),
]
