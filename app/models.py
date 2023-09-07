from django.db import models

# Create your models here.

class Employee(models.Model):

    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    phone = models.CharField(max_length=30)

    class Meta:
        db_table = "employees"