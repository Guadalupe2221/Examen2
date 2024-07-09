from rest_framework import serializers
from .models import Pendientes

class PendienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendientes
        fields = ['id', 
                  'title',
                  'description',
                  'is_done',
                  'user',
                  'created_at',
                  'updated_at'
                ]