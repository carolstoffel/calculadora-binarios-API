from rest_framework.serializers import ModelSerializer
from binarios.models import CalculaBinarios
from rest_framework.response import Response
from operator import add, sub, floordiv, mul, mod


class BinariosSerializer(ModelSerializer):

    class Meta:
        model = CalculaBinarios
        fields = ('id', 'operacao', 'numero1', 'numero2')

    def to_representation(self, data):
        data = super(BinariosSerializer, self).to_representation(data)
        soma = int(data['numero1'], 2)+int(data['numero2'], 2)
        data['binario'] = bin(soma)[2:]
        '''
        if data['operacao'] == '+':
            r = add(data['numero1'], data['numero2'])
        elif data['operacao'] == '-':
            r = sub(data['numero1'], data['numero2'])
        elif data['operacao'] == '/':
            r = floordiv(data['numero1'], data['numero2'])
        elif data['operacao'] == '*':
            r = mul(data['numero1'], data['numero2'])
        elif data['operacao'] == '%':
            r = mod(data['numero1'], data['numero2'])
        data['resposta'] = r'''
        return data
