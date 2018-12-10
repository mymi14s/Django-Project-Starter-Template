"""
Author: Anthony C. Emmanuel
Title: Django Project Starter Template
Version: 1.0.0
Language: Python 3.6
Date: 07-12-2018
License: 3-clause BSD
"""

from django.contrib import admin
from setting.models import Setting
# Register your models here.

class AdminSetting(admin.ModelAdmin):
    list_display = ['site_name', 'site_title','site_email', 'site_phone',  'site_address']
    list_filter = ['site_name', 'site_title', 'site_email', 'site_phone', 'site_address']
    search_fields = ['site_name', 'site_title', 'site_email',  'site_phone', 'site_phone']
    #list_editable = ['full_name', 'email', 'dob', 'phone_number']


register = admin.site.register
register(Setting, AdminSetting)
