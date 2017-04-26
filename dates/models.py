from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Nahual(models.Model):
    nombre = models.CharField(max_length=20)
    color = models.CharField(max_length=15, null=True, blank=True)
    simbolos = models.TextField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    foto = ThumbnailerImageField(
        upload_to="iconos_nahual",
        null=True,
        blank=True,
        editable=True,)

    class Meta:
        verbose_name = "Nahual"
        verbose_name_plural = "Nahuales"

    def __str__(self):
        return self.nombre

