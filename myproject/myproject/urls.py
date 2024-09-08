"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calculations import views  # Adjust this import based on your project structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/split_evenly/', views.split_evenly, name='split_evenly'),
    path('api/split_unevenly/', views.split_unevenly, name='split_unevenly'),
    path('api/split_evenly_with_tax_tip/', views.split_evenly_with_tax_tip, name='split_evenly_with_tax_tip'),
    path('api/split_evenly_with_discount/', views.split_evenly_with_discount, name='split_evenly_with_discount'),
    path('api/split_with_shared_items/', views.split_with_shared_items, name='split_with_shared_items'),
]

