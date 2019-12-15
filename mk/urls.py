"""informer_batyr URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

from mk import views
from mk.views import ChecklistView, MkReport, MkReportEtc, mk_nkro_report

urlpatterns = [
    path('check_list_mk/', views.form_check_list_mk, name='check_list_mk_url'),
    path('mk_report/', MkReport.as_view(), name='mk_report_url'),
    # path('mk_etc_report/', MkReportEtc.as_view(), name='mk_etc_report_url'),
    path('mk_nkro_report/', mk_nkro_report, name='mk_nkro_report_url'),
    path('quality_report/<str:slug>/', ChecklistView.as_view(), name='view_checklist_url'),
    path('search_shop/', views.search_shop, name='mk_search_shop_url'),
    path('search_sv/', views.search_date, name='mk_search_sv_url'),

]
