from rest_framework import generics
from .models import Pendientes
from .serializers import PendienteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class PendientesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pendientes.objects.all()
    serializer_class = PendienteSerializer

class PendientesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pendientes.objects.all()
    serializer_class = PendienteSerializer

@api_view(['GET'])
def pendiente_ids(request):
    ids = Pendientes.objects.values_list('id', flat=True)
    return Response(ids)

@api_view(['GET'])
def pendiente_ids_titles(request):
    pendientes = Pendientes.objects.values('id', 'title')
    return Response(pendientes)

@api_view(['GET'])
def pendiente_unresolved(request):
    pendientes = Pendientes.objects.filter(is_done=False).values('id', 'title')
    return Response(pendientes)

@api_view(['GET'])
def pendiente_resolved(request):
    pendientes = Pendientes.objects.filter(is_done=True).values('id', 'title')
    return Response(pendientes)

@api_view(['GET'])
def pendiente_ids_userids(request):
    pendientes = Pendientes.objects.values('id', 'user_id')
    return Response(pendientes)

@api_view(['GET'])
def pendiente_resolved_userids(request):
    pendientes = Pendientes.objects.filter(is_done=True).values('id', 'user_id')
    return Response(pendientes)

@api_view(['GET'])
def pendiente_unresolved_userids(request):
    pendientes = Pendientes.objects.filter(is_done=False).values('id', 'user_id')
    return Response(pendientes)