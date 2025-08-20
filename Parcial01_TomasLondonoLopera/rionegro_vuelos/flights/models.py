from django.db import models
from django.core.validators import MinValueValidator


class Flight(models.Model):
    TYPE_NACIONAL = 'Nacional'
    TYPE_INTERNACIONAL = 'Internacional'

    TYPE_CHOICES = [
        (TYPE_NACIONAL, 'Nacional'),
        (TYPE_INTERNACIONAL, 'Internacional'),
    ]

    name = models.CharField('Nombre', max_length=100)
    type = models.CharField('Tipo', max_length=13, choices=TYPE_CHOICES)
    price = models.DecimalField(
        'Precio', max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    class Meta: #Como se ordena
        verbose_name = 'Vuelo'
        verbose_name_plural = 'Vuelos'
        ordering = ['price'] #Ordenar por prcio

    def __str__(self):
        return f"{self.name} ({self.type}) - ${self.price}"
