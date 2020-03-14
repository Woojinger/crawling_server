from django.db import models

# Create your models here.

class Amazon(models.Model):
    Name = models.CharField(max_length=200)
    Brand = models.CharField(max_length=100, default="NA")
    Rank = models.CharField(max_length=10)
    Selected_category = models.CharField(max_length=200)
    Parent_category = models.CharField(max_length=200)
    Date = models.CharField(max_length=100)

    def __str__(self):
        return self.Brand+"_"+self.Rank+"_"+self.Selected_category+"_"+self.Date


class Gevolution(models.Model):
    Name = models.CharField(max_length=200)
    Rank = models.CharField(max_length=10)
    Company = models.CharField(max_length=200)
    Date = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)

    def __str__(self):
        return self.Name+"_"+self.Rank+"_"+self.Category+"_"+self.Date