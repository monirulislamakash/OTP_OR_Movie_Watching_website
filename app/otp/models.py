from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Contant(models.Model):
    titel=models.CharField(max_length=40,default="")
    video=models.CharField(max_length=10000,default="")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    thmnul=models.ImageField(upload_to="static/thumnel/",default="")
    download=models.CharField(max_length=10000,default="")
    def __str__(self):
        return self.titel