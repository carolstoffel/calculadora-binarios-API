from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CalculaBinarios(models.Model):

    def validate_binarios(numero):
        # Don't allow draft entries to have a pub_date.
        for i in numero:
            if i in '10':
                pass
            else:
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
    numero1 = models.CharField(max_length=8, validators=[validate_binarios])
    numero2 = models.CharField(max_length=8, validators=[validate_binarios])

    def __str__(self):
        return self.numero1, self.operacao, self.numero2
