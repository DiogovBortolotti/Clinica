from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from agendamentos.api.serializers import (AgendamentoDetalhesSerializer,
                                          AgendamentoSerializer)
from agendamentos.models import Agendamentos


class AgendamentosViewSet(ModelViewSet):
    queryset = Agendamentos.objects.all().order_by('data_hora')
    serializer_class = AgendamentoSerializer
   

    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None, *args, **kwargs):
        queryset = Agendamentos.objects.filter(pk=pk)
        self.serializer_class = AgendamentoDetalhesSerializer
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)