from django.db import models

# Create your models here.

class Parent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)


    def __str__(self):
        return self.name