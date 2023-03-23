from django.db import models

from agendamentos.models import Agendamentos

# Create your models here.


class Historicos(models.Model):
    id_historico = models.AutoField(primary_key=True)
    data = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    sintomas = models.TextField(max_length=200, blank=True, null=True)
    duracao_sintomas = models.CharField(max_length=100, blank=True, null=True)
    local_dor = models.CharField(max_length=100, blank=True, null=True)
    tipo_dor = models.CharField(max_length=100, blank=True, null=True)
    conclusao = models.TextField(max_length=300, blank=False, null=False)
    id_agendamento = models.ForeignKey(Agendamentos, on_delete=models.CASCADE, related_name='historicos', blank=False, null=False)
    
    class Meta:
        managed=True
        db_table = 'historicos'