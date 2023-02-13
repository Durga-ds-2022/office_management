from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Department, Role
from datetime import datetime
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request, 'index.html')

def add_emp(request):
    if request.method=="POST":
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        dept= int(request.POST['dept'])
        salary= int(request.POST['salary'])
       
        role= request.POST['role']
        phone_number= int(request.POST['phone_number'])

        emp= Employee.objects.create(
        first_name= first_name,
        last_name= last_name,
        dept_id= dept,
        salary= salary,
       
        role_id= role,
        phone= phone_number,
        hire_date= datetime.now()
        )
        return redirect('home')

    obj= Department.objects.all()
    obj1= Role.objects.all()
    context= {
        'depts': obj,
        'roles': obj1
       
    }
    
    return render(request, 'add_emp.html', context)

def all_emp(request):
    obj=Employee.objects.all()
    context={
        'data': obj
    }
    return render(request, 'all_emp.html', context)


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed= Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee has been Remove Successfullly")
        except Exception as e:
            return HttpResponse(e)    
    obj= Employee.objects.all()
    context= {'emp': obj}
    return render(request, 'remove_emp.html', context )

def update_emp(request, emp_id):
    obj = Employee.objects.get(id= emp_id)
    if request.method=="POST":
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        dept = int(request.POST['dept'])
        salary= int(request.POST['salary'])
        role= int(request.POST['role'])
        phone_number= int(request.POST['phone_number'])
        obj.first_name= first_name
        obj.last_name= last_name
        obj.dept_id= dept
        obj.salary= salary
        obj.role_id= role
        obj.phone= phone_number
        obj.save()
        return redirect('home')
   
    depts= Department.objects.all()
    roles = Role.objects.all()
    context= {
        'emp': obj,
        'depts': depts,
        'roles': roles
        
    }

    return render(request, 'update_emp.html', context)


def filter_emp(request):
    emps = Employee.objects.all()
    if request.method=="POST":
        name= request.POST['name']
        dept= request.POST['dept']
        role= request.POST['role']
        
        if name:
            emps= emps.filter(Q(first_name__icontains= name)| Q(last_name__icontains=name))
        if dept:
            emps= emps.filter(dept__name == dept)
        if role:
            emps= emps.filter(role__name == role)
        context= {
            'data': emps
        }    
        return render(request, 'all_emp.html', context)

    return render(request, 'filter_emp.html')


