from django.db import models

from historicos.models import Historicos
from pacientes.models import Pacientes

# Create your models here.

def imagens_historico(instance, filename):
    return '/'.join(('historico', str(instance.id_historico.id_historico), filename))

def imagens_paciente(instance, filename):
    return '/'.join(('paciente', str(instance.id_paciente.id_paciente), filename))



class ImagensHistoricos(models.Model):
    id_imagem_historico = models.AutoField(primary_key=True)
    imagem_historico = models.ImageField(upload_to=imagens_historico, blank=True, null=True)
    id_historico = models.ForeignKey(Historicos, on_delete=models.CASCADE,  blank=False, null=False, related_name='imagens')
    
class ImagensPacientes(models.Model):
    id_imagem_paciente = models.AutoField(primary_key=True)
    imagem_paciente = models.ImageField(upload_to=imagens_paciente, blank=True, null=True)
    id_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE, blank=False, null=False, related_name='imagens_paciente')
    
    
