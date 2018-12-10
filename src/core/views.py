"""
Author: Anthony C. Emmanuel
Title: Django Project Starter Template
Version: 1.0.0
Language: Python 3.6
Date: 07-12-2018
License: 3-clause BSD
"""

from django.views.generic import TemplateView

class Index(TemplateView):
    """View for the index page"""

    template_name = 'core/index.html'

    def get_object(self):
        return self.request.user
