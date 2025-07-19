# backend/yieldapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_csv, name='upload_csv'),
    path('dashboard/', views.dashboard_operator, name='dashboard_operator'),
    path('mstd/dashboard/', views.dashboard_mstd, name='dashboard_mstd'),
]
