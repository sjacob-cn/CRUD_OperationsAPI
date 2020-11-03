from django.db import models

# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=20)
    emp_id=models.IntegerField()
    salary=models.IntegerField()

    def __str__(self):
        return self.name
