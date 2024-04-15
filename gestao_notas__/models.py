from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    birth_date = models.DateField()
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.name
