from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CalculaBinarios(models.Model):

    def validate_binarios(numero):
        # função que valida se o numero inserido pelo usuario é 0 ou 1
        for i in numero:
            if i not in '10':
                raise ValidationError(
                    _('Não é um binário. Por favor digite 0 ou 1.'))

    OPERACOES = (
        ('+', 'Soma'),
        ('-', 'Subtracão'),
        ('*', 'Multiplicação'),
        ('/', 'Divisão'),
        ('%', 'Resto da divisão'),
    )
    operacao = models.CharField(max_length=1, choices=OPERACOES)
    # Nas variaveis numero1 e numero2, definido o tamanho maximo 8,
    # 255 em binario ocupam 8 caracteres, 256 ocupam 9, servindo
    # entao de validacao
    numero1 = models.CharField(max_length=8, validators=[
                               validate_binarios])
    numero2 = models.CharField(max_length=8, validators=[
                               validate_binarios])

    def __str__(self):
        return self.numero1, self.operacao, self.numero2
