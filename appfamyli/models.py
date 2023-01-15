from django.db import models

# Create your models here.

class Town(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Town, on_delete=models.CASCADE)


    def __str__(self):
        return self.name