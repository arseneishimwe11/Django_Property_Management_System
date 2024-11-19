from django.contrib import admin
from .models import Property

admin.site.register(Property)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'size_in_sqft', 'rent', 'is_available')
    search_fields = ('name', 'address')

