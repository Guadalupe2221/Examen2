from django.urls import path
from .views import (
    PendientesListCreateAPIView, 
    PendientesDetailAPIView,
    pendiente_ids,
    pendiente_ids_titles,
    pendiente_unresolved,
    pendiente_resolved,
    pendiente_ids_userids,
    pendiente_resolved_userids,
    pendiente_unresolved_userids
)

urlpatterns = [
    path('pendientes/', PendientesListCreateAPIView.as_view(), name='pendiente-list-create'),
    path('pendientes/<int:pk>/', PendientesDetailAPIView.as_view(), name='pendiente-detail'),
    path('pendientes/ids/', pendiente_ids, name='pendiente-ids'),
    path('pendientes/ids_titles/', pendiente_ids_titles, name='pendiente-ids-titles'),
    path('pendientes/unresolved/', pendiente_unresolved, name='pendiente-unresolved'),
    path('pendientes/resolved/', pendiente_resolved, name='pendiente-resolved'),
    path('pendientes/ids_userids/', pendiente_ids_userids, name='pendiente-ids-userids'),
    path('pendientes/resolved_userids/', pendiente_resolved_userids, name='pendiente-resolved-userids'),
    path('pendientes/unresolved_userids/', pendiente_unresolved_userids, name='pendiente-unresolved-userids'),
]