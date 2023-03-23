from rest_framework import serializers

from imagens.models import ImagensHistoricos, ImagensPacientes


class ImagensHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagensHistoricos
        fields = '__all__' 
        
class ImagensPacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagensPacientes
        fields = ['id_imagem_paciente', 'imagem_paciente']