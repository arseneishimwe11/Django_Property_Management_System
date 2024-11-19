from django.shortcuts import render
from django.db.models import Sum
from properties.models import Property
from tenants.models import Tenant, MaintenanceRequest
from dashboard.models import DashboardMetrics


def dashboard_view(request):
    # Data for the dashboard
    total_properties = Property.objects.count()
    active_tenants = Tenant.objects.filter(active=True).count()
    pending_requests = MaintenanceRequest.objects.filter(status="Pending").count()
    monthly_income = Property.objects.aggregate(total_rent=Sum('monthly_rent'))['total_rent'] or 0.00

    # Update metrics in database
    metrics, created = DashboardMetrics.objects.update_or_create(
        id=1,  # Assume a single row
        defaults={
            "total_properties": total_properties,
            "active_tenants": active_tenants,
            "pending_maintenance_requests": pending_requests,
            "monthly_income": monthly_income,
        },
    )

    context = {
        "metrics": metrics,
    }
    return render(request, "dashboard/dashboard.html", context)
