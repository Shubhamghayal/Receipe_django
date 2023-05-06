from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

class Product(models.Model):
    pass

class car(models.Model):
    car_name=models.CharField(max_length=500)
    car_speed=models.IntegerField()
    def __str__(self):
        return self.car_name
