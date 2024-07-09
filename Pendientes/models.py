from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pendientes(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta: 
        db_table = 'pendientes'
