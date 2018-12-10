""" Register template global settings data """

from django import template

register = template.Library()

@register.filter()
def class_name(value):
    return value.__class__.__name__
