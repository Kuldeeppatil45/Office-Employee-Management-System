from django.shortcuts import render,HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context ={
        'emps':emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        salary = int(request.POST['salary'])
        bouns = int(request.POST['bouns'])
        phone = request.POST['phone']
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(First_name=First_name,Last_name=Last_name,salary=salary,bouns=bouns,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added succesfully")
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("An Exception occured! Employee has not been added")

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_br_removed = Employee.objects.get(id = emp_id)
            emp_to_br_removed.delete()
            return HttpResponse("Employee Removed Succesfully")
        except:
            return HttpResponse("Please enter a valid employee ID.")
    emps = Employee.objects.all()
    context ={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(First_name__icontains = name) | Q(Last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)
        context ={
        'emps':emps
        }
        return render(request,'view_all_emp.html',context)
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("An Exception Occured")