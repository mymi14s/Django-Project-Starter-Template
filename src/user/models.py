"""
Author: Anthony C. Emmanuel
Title: Django Project Starter Template
Version: 1.0.0
Language: Python 3.6
Date: 07-12-2018
License: 3-clause BSD
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import SelectDateWidget
# Create your models here.

class CustomUser(AbstractUser):
    """Customized user model"""

    slug = models.SlugField(allow_unicode=True, unique=True)
    photo = models.ImageField(upload_to='users', null=True)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):

        if(self.username == 'admin'):
            """Change slug to avoid url conflict with cpanel if user is admin"""
            self.slug = 'admin_user'
        else:
            self.slug = self.username

        super().save(*args, **kwargs)
    #
    # def get_absolute_url(self):
    #     return reverse_lazy('/', kwargs={'slug'})
