"""
Author: Anthony C. Emmanuel
Title: Django Project Starter Template
Version: 1.0.0
Language: Python 3.6
Date: 07-12-2018
License: 3-clause BSD
"""

from django.db import models

# Create your models here.

class Setting(models.Model):
    """General system settings model."""

    site_name = models.CharField(blank=True, max_length=100)
    site_title = models.CharField(blank=True, max_length=100)
    site_phone = models.CharField(blank=True, max_length=25)
    site_email = models.EmailField(unique=True, max_length=100)
    site_address = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.site_name
