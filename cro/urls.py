"""informer_batyr URL Configuration

"""
from django.urls import path

from cro.views import TabInvView, InventResultReport, InventStatsReport
from . import views

urlpatterns = [
    path('table_inv/', views.form_table_inv, name='table_inv'),
    path('invent_report/', InventResultReport.as_view(), name='invent_report_url'),
    # path('invent_report_stats/', InventStatsReport.as_view(), name='invent_report_stats_url'),
    path('invent_report/<str:slug>/', TabInvView.as_view(), name='view_tab_invent_url'),
    path('search_shop/', views.search_shop, name='search_shop_url'),
]
