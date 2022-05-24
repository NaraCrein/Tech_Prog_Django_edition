from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="")

class TUser(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=12)



