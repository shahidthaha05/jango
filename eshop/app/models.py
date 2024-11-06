from django.db import models

# Create your models here.

class Product(models.Model):
    pro_id=models.TextField()
    name=models.TextField()
    price=models.IntegerField()
    ofr_price=models.IntegerField()
    img=models.FileField()
    dis=models.TextField()