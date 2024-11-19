from django.db import models


class DashboardMetrics(models.Model):
    total_properties = models.PositiveIntegerField(default=0)
    active_tenants = models.PositiveIntegerField(default=0)
    pending_maintenance_requests = models.PositiveIntegerField(default=0)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Metrics as of {self.last_updated}"

