import os
import uuid

from django.db import models
from django.utils.text import slugify


class MeasureUnit(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


def image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.name)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/products/", filename)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description_cs = models.TextField()
    description_en = models.TextField()
    description_de = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=image_file_path)

    def __str__(self):
        return self.name

