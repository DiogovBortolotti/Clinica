from rest_framework import viewsets
from rest_framework.response import Response

from imagens.api.serializers import (ImagensHistoricoSerializer,
                                     ImagensPacientesSerializer)
from imagens.models import ImagensHistoricos, ImagensPacientes


class ImagemViewSet(viewsets.ModelViewSet):
    serializer_class = ImagensHistoricoSerializer
    queryset = ImagensHistoricos.objects.all()
    

class ImagemPacientesViewSet(viewsets.ModelViewSet):
    serializer_class = ImagensPacientesSerializer
    queryset = ImagensPacientes.objects.all()
    
