from django.db import models

# Create your models here.
class Collection(models.Model):
    collection_name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    collcover = models.CharField(max_length=1000)
    def __str__(self):
        return self.collection_name

class Piece(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    type =models.CharField(max_length=100)
    year =models.IntegerField()
    artist =models.CharField(max_length=100)
    piececover =models.CharField(max_length=1000)
    def __str__(self):
        return self.title
