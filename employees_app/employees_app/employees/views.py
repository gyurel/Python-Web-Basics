from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from employees_app.employees.models import Department, Employee


def home(request):
    print(request.user)
    return HttpResponse("This is home")


def department_details(request, id):
    return HttpResponse(f"This is department {id}")


def list_departments(request):
    context = {
        # 'departments': Department.objects.filter(name__iendswith='app'),
        'departments': Department.objects.prefetch_related('employee_set').all(),
        'employees': Employee.objects.all(),
    }
    return render(request, 'list_departments.html', context)
    # return HttpResponse("This is a list of departments")
