from rest_framework import serializers
from ces import models


class ObjetoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Objeto
        fields = ('id', 'nome', 'tipoObjeto_id', 'status')
        depth = 1


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Usuario
        fields = ('id', 'name', 'email', 'profileName')
        depth = 1


class MovimentacaoSerializer(serializers.ModelSerializer):
    usuario_id = UsuarioSerializer()
    reserva = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = models.Movimentacao
        fields = ('id', 'retirada', 'devolucao', 'reserva', 'objeto_id', 'usuario_id', 'status')
        depth = 2


class TransferenciaSerializer(serializers.ModelSerializer):
    movimentacao_id_origem = MovimentacaoSerializer()
    movimentacao_id_destino = MovimentacaoSerializer()

    class Meta:
        model = models.Transferencia
        fields = '__all__'
        depth = 1
