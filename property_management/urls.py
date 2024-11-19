from django.contrib import admin
from django.urls import path, include
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('admin/', admin.site.urls),
    path('properties/', include('properties.urls')),
    path('tenants/', include('tenants.urls')),
    path('users/', include(('Users.urls', 'users'), namespace='users')),
    path('dashboard/', include('dashboard.urls')),
]
