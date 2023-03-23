from rest_framework.serializers import ModelSerializer

from agendamentos.models import Agendamentos
from historicos.api.serializers import HistoricoDetalheSerializer


class AgendamentoSerializer(ModelSerializer):
    class Meta:
        model = Agendamentos
        fields = '__all__'

class AgendamentoDetalhesSerializer(ModelSerializer):
    historicos = HistoricoDetalheSerializer(many=True, read_only=True)
    class Meta:
        model = Agendamentos
        fields = ['id_agendamento', 'data_hora', 'data_criacao', 'cancelado',  'obs', 'tipo', 'historicos']
