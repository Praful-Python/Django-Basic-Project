"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="shophome"),
    path("dashboard/", views.dashboard, name="shop"),
    path("form/", views.form, name="form"),
    path("table/", views.table, name="table"),
    path("dashboard/<int:cus_id>", views.customer_id, name='QuickView'),
    path("delete/<int:cus_id>", views.delete_patient, name='delete_patient')
]
