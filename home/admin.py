from django.contrib import admin
from django.apps.registry import apps
# Register your models here.
admin.site.register(apps.all_models['home'].values())
# Register your models here.
