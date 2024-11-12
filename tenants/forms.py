from django import forms
from .models import Tenant, MaintenanceRequest


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'email', 'phone', 'claim_date', 'property']
        widgets = {
            'claim_date': forms.DateInput(attrs={'type': 'date'}),
        }


class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = '__all__'

