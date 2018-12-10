"""
Author: Anthony C. Emmanuel
Title: Django Project Starter Template
Version: 1.0.0
Language: Python 3.6
Date: 07-12-2018
License: 3-clause BSD
"""

from django import template

register = template.Library()

@register.filter()
def class_name(value):
    return value.__class__.__name__
