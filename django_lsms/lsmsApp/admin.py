"""
Developed by MASA
All Rights Reserved.
"""

from django.contrib import admin
from lsmsApp import models
from django.apps import apps

for model in apps.get_models():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
