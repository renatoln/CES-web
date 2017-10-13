from rest_framework import serializers
from ces import models


class ObjetoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Objeto
        fields = ('id', 'nome', 'tipoObjeto_id', 'status')
        depth = 1


class MovimentacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Movimentacao
        fields = ('id', 'retirada', 'devolucao', 'objeto_id', 'usuario_id', 'status')
        depth = 1


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Usuario
        fields = ('id', 'name', 'email', 'profileName')
        depth = 1


class TransferenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transferencia
        fields = '__all__'
        depth = 1
