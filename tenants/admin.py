from django.contrib import admin
from .models import Tenant, MaintenanceRequest

admin.site.register(Tenant)
admin.site.register(MaintenanceRequest)