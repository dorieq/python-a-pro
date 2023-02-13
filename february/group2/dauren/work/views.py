from django.http import HttpResponse
from .models import Employee

import json
import requests

# Create your views here.
def v(request):
    return HttpResponse('Hello World!')

def create(request):
    e = Employee()
    e.firstname = 'Ivan'
    e.secondname = 'Popov'
    e.salary = 300
    e.exp = 3
    e.department = 'IT'
    e.save()

def get(request):
    employees = Employee.objects.all()
    answer = ''
    for e in employees:
        answer = answer + str(e) + '\n'
    return HttpResponse(answer)

def delete(request):
    Employee.objects.filter(firstname='Ivan').delete()
    return HttpResponse('Succesfully deleted')
