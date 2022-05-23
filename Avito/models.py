from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="")
    image2 = models.ImageField(upload_to="")
    image3 = models.ImageField(upload_to="")
    desc = models.CharField(max_length=255)
    seller = models.CharField(max_length=255)


