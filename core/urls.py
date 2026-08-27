from django.urls import path

from .views import dashboard_view, platform_info_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('info/', platform_info_view, name='platform_info'),
]
