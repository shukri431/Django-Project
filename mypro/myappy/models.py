from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.firstName} {self.lastname} - {self.email} - {self.age}"
    