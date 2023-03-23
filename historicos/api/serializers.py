
from rest_framework.serializers import ModelSerializer

from historicos.models import Historicos
from imagens.api.serializers import ImagensHistoricoSerializer


class HistoricosSerializer(ModelSerializer):

    class Meta:
        model = Historicos
        fields = '__all__'


class HistoricoDetalheSerializer(ModelSerializer):
    imagens = ImagensHistoricoSerializer(many=True, read_only=True)
    class Meta:
        model = Historicos
        fields = ['id_historico', 'id_agendamento', 'sintomas', 'duracao_sintomas', 'local_dor', 'tipo_dor', 'conclusao', 'imagens']
        