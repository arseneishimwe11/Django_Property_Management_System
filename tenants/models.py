from django.db import models
from django.utils import timezone
from properties.models import Property


class Tenant(models.Model):
    # user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    properties = models.ManyToManyField(Property, related_name='tenants')   # A tenant can rent multiple properties
    claim_date = models.DateField(default=timezone.now)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MaintenanceRequest(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'Maintenance request by {self.tenant.name}'
