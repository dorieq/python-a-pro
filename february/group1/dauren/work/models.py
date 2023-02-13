from django.db import models

GRADE = [
    ('JN', 'Junior'),
    ('MD', 'Middle'),
    ('SN', 'Senior'),
    ('TL', 'Team lead')
]


class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)
    salary = models.IntegerField()
    exp = models.IntegerField(default=0)
    grade = models.CharField(max_length=2, choices=GRADE)

    def __str__(self) -> str:
        return self.firstname + ' ' + self.secondname