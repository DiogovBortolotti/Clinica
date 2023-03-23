
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from agendamentos.api.serializers import AgendamentoDetalhesSerializer
#from historicos.api.serializers import HistoricosSerializer
from imagens.api.serializers import ImagensPacientesSerializer
from pacientes.models import Pacientes


class PacientesSerializer(ModelSerializer):
    class Meta:
        model = Pacientes
        fields = ['id_paciente', 'nome', 'cpf', 'data_nasc', 'endereco', 'rua_endereco', 'bairro', 'cep', 'data_cadastro']
        
        
class PacientesDetalhesSerializer(ModelSerializer):
    agendamentos = AgendamentoDetalhesSerializer(many=True, read_only=True)# 1 para muitos não pode alterar 
    #historicos = HistoricosSerializer(many=True, read_only=True) 
    #imagens_paciente = ImagensPacientesSerializer(many=True, read_only=True) # a palavra que recebe vai ficar ali embaixo # eu poderia trazer em  source='imagens_paciente'
    ultima_imagem = ImagensPacientesSerializer(read_only=True) # a variavel recebe devido eu ter colocado um def em model do paciente para trazer somente a ultima informação
    class Meta:
        model = Pacientes
        fields = ['id_paciente', 'nome', 'cpf', 'data_nasc', 'endereco', 'rua_endereco', 'bairro', 'cep', 'data_cadastro', 'agendamentos', 'ultima_imagem']#historicos
        
# ideia colocar agendamento detalhes e colocar junto ali 