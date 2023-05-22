from uuid import uuid4

from django.db import models


def generate_filename(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{str(uuid4())}.{ext}"
    return f"{filename}"


class ImageModel(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to=generate_filename
    )

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
