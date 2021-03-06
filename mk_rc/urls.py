"""informer_batyr URL Configuration

"""
from django.contrib import admin
from django.urls import path, include, re_path

from mk_rc import views, polls

urlpatterns = [
    path('vsd/', views.vsd, name='vsd_url'),
    path('vsd_filtr/', views.vsd_filtr, name='vsd_filtr_url'),
    path('bd_vsd/', views.bd_vsd, name='bd_vsd_url'),
    path('form_bd_vsd', views.form_bd_vsd, name='form_bd_vsd_url'),
    path('edit_bd_vsd/<int:id>', views.edit_bd_vsd, name='edit_bd_vsd_url'),
    path('delete_bd_vsd/<int:id>', views.delete_bd_vsd, name='delete_bd_vsd_url'),

    path('uplink/', polls.upload, name='uplink'),
    path('exchange/(.*)', polls.exchange, name="exchange"),
    path('import_1c/', polls.import_sheet, name="import_url"),

    path('api_vsd_merc/', views.ApiVsdMerc.as_view(), name='api_vsd_merc_url'),
    path('api_vsd_merc/<int:id_vsd>', views.ApiVsdMerc.as_view(), name='api_vsd_merc_detail_url'),
]
