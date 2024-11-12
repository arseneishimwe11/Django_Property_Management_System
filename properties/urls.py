from django.urls import path
from .views import property_list, property_create, property_update, property_delete, login_view, logout_view

urlpatterns = [
    path('', property_list, name='property_list'),
    path('create/', property_create, name='property_create'),
    path('update/<int:pk>/', property_update, name='property_update'),
    path('delete/<int:pk>/', property_delete, name='property_delete'),
]
