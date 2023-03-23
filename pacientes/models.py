from django.db import models


# Create your models here.
class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=False)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    data_nasc = models.DateField(blank=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    rua_endereco = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=11, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)




    class meta:
        managed = True
        db_table = 'pacientes'
        
    def ultima_imagem(self):
        try:
            return self.imagens_paciente.order_by('-id_imagem_paciente')[0]
        except IndexError:
            return None