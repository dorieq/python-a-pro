from django.http import HttpResponse
from .models import Employee

def v(request):
    return HttpResponse("abcd")

def save(request):
    e = Employee()
    e.firstname = 'Arman'
    e.secondname = 'Serikov'
    e.exp = 5
    e.salary = 500000
    e.save()
    return HttpResponse(e)

def delete(request):
    employees = Employee.objects.filter(firstname='Arman')
    print(employees)
    if not employees:
        return HttpResponse('Nothing to delete')
    employees.delete()
    return HttpResponse('Succesfully deleted')