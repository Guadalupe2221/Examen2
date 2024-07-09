from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pendientes/ids/', views.pendientes_ids, name='pendientes-ids'),
    path('pendientes/ids_titles/', views.pendientes_ids_titles, name='pendientes-ids-titles'),
    path('pendientes/unresolved/', views.pendientes_unresolved, name='pendientes-unresolved'),
    path('pendientes/resolved/', views.pendientes_resolved, name='pendientes-resolved'),
    path('pendientes/ids_userids/', views.pendientes_ids_userids, name='pendientes-ids-userids'),
    path('pendientes/resolved_userids/', views.pendientes_resolved_userids, name='pendientes-resolved-userids'),
    path('pendientes/unresolved_userids/', views.pendientes_unresolved_userids, name='pendientes-unresolved-userids'),
]

