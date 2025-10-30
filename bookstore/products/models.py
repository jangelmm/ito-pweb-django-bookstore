from django.db import models
from django.core.validators import MinValueValidator  # ← Agregar este import
from decimal import Decimal

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.FileField(
        upload_to='products/', 
        blank=True, 
        null=True,
        verbose_name="Archivo adjunto"
    )
    price = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
        verbose_name="Precio",
        validators=[MinValueValidator(Decimal('0.01'))]  # ← Corregido
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"