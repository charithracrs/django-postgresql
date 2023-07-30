from django.db import models

# Create your models here.
class Acrylic(models.Model):
    # id: int
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price =  models.IntegerField()
    sale = models.BooleanField(default=False)