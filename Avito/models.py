from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    place = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="images/", null=True)
    image2 = models.ImageField(upload_to="images/", null=True)
    image3 = models.ImageField(upload_to="images/", null=True)
    desc = models.CharField(max_length=255, null=True)
    seller = models.CharField(max_length=255, null=True)


