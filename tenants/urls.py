from django.urls import path
from .views import tenant_list, tenant_create, tenant_update, tenant_delete, maintenance_request_create

urlpatterns = [
    path('tenants/', tenant_list, name='tenant_list'),
    path('create/', tenant_create, name='tenant_create'),
    path('update/<int:pk>/', tenant_update, name='tenant_update'),
    path('delete/<int:pk>/', tenant_delete, name='tenant_delete'),
    path('maintenance-request/create/', maintenance_request_create, name='maintenance_request_create'),
]