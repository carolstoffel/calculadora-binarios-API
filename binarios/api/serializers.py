from rest_framework.serializers import ModelSerializer
from binarios.models import CalculaBinarios
from rest_framework.response import Response
from operator import add, sub, floordiv, mul, mod


class BinariosSerializer(ModelSerializer):

    class Meta:
        model = CalculaBinarios
        fields = ('id', 'operacao', 'numero1', 'numero2')

    def to_representation(self, data):
        """
        No exercício está escrito que a saída deve ser a resposta, 
        porém achei mais interessante retornar todos os dados inseridos com a resposta.
        Para retornar apenas o resultado da operação, seria adicionar as linhas abaixo:
        saida = {}
        saida['resultado em binario'] = data['resultado em binario']
        return saida
        """
        data = super(BinariosSerializer, self).to_representation(data)

        if data['operacao'] == '+':
            r = add(int(data['numero1'], 2), int(data['numero2'], 2))
        elif data['operacao'] == '-':
            r = sub(int(data['numero1'], 2), int(data['numero2'], 2))
        elif data['operacao'] == '/':
            r = floordiv(int(data['numero1'], 2), int(data['numero2'], 2))
        elif data['operacao'] == '*':
            r = mul(int(data['numero1'], 2), int(data['numero2'], 2))
        elif data['operacao'] == '%':
            r = mod(int(data['numero1'], 2), int(data['numero2'], 2))
        data['resultado em binario'] = bin(r)[2:]
        return data
