
"""
Author: Anthony C. Emmanuel
Title: Django Project Starter Template
Version: 1.0.0
Language: Python 3.6
Date: 07-12-2018
License: 3-clause BSD
"""
from django.contrib import admin
from user.models import CustomUser
# Register your models here.

class AdminCustomUser(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email','date_joined']
    list_filter = ['username', 'first_name', 'last_name', 'email','date_joined']
    search_fields = ['username', 'first_name', 'last_name', 'email','date_joined']
    #list_editable = ['email']

register = admin.site.register #shorten the module name
register(CustomUser, AdminCustomUser)
