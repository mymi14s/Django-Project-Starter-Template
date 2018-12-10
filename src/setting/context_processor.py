"""
Author: Anthony C. Emmanuel
Title: Django Project Starter Template
Version: 1.0.0
Language: Python 3.6
Date: 07-12-2018
License: 3-clause BSD
"""

from django.utils.functional import SimpleLazyObject
from setting.models import Setting
import datetime

def setting(request):
    """Context processor function for global template content display."""

    data = Setting.objects.filter(id=1)[0]
    data.year = str(datetime.date.today())[:4]
    #print(data.year, data.site_title, data.site_phone)

    return {'global_settings':data, 'request':request}
