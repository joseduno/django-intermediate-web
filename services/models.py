from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    subtitle = models.CharField(max_length=50, verbose_name='Subtítulo')
    image = models.ImageField(upload_to='service', verbose_name='Imagen')
    description = models.TextField(verbose_name='Descripción')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-updated']

    def __str__(self):
        return title