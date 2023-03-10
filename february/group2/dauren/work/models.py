from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)
    exp = models.IntegerField()
    department = models.CharField(max_length=50)
    salary = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.firstname + " " + self.secondname