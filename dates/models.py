from django.db import models
from django.urls import reverse_lazy
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.text import slugify


class Nahual(models.Model):
    nombre = models.CharField(max_length=20)
    color = models.CharField(max_length=15, null=True, blank=True)
    codigo = models.CharField(max_length=7, null=True, blank=True)
    caracteristicas = models.TextField(null=True, blank=True)
    interpretacion = models.TextField(null=True, blank=True)
    aplicacion = models.TextField(null=True, blank=True)
    simbolos = models.TextField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    slug = models.SlugField(max_length=40, unique=True, null=True, blank=True)

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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Nahual, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('nahual_detail', kwargs={'slug': self.slug})
