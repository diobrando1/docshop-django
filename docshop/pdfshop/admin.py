"""
pdfshop admin
"""

from django.contrib import admin
from .models import PDF
from .models import Profile

admin.site.register(Profile)
admin.site.register(PDF)
