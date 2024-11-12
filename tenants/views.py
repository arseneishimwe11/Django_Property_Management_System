from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tenant, MaintenanceRequest
from .forms import TenantForm, MaintenanceRequestForm
import logging
logger = logging.getLogger(__name__)


@login_required(login_url="/users/login")
def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenants/tenant_list.html', {'tenants': tenants})


@login_required(login_url="/users/login")
def tenant_create(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            tenant = form.save(commit=False)
            # tenant.user = request.user
            tenant.save()
            form.save_m2m()
            return redirect('tenant_list')
    else:
        form = TenantForm()
        logger.error("Form errors: %s", form.errors)
    return render(request, 'tenants/tenant_form.html', {'form': form})


@login_required(login_url="/users/login")
def tenant_update(request, pk):
    tenant = Tenant.objects.get(pk=pk)
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm(instance=tenant)
    return render(request, 'tenants/tenant_form.html', {'form': form})


@login_required(login_url="/users/login")
def tenant_delete(request, pk):
    tenant = Tenant.objects.get(pk=pk)
    if request.method == 'POST':
        tenant.delete()
        return redirect('tenant_list')
    return render(request, 'tenants/tenant_confirm_delete.html', {'tenant': tenant})


@login_required(login_url="/users/login")
def maintenance_request_create(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = MaintenanceRequestForm()
    return render(request, 'tenants/maintenance_request_form.html', {'form': form})