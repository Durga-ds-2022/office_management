from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name+", " + self.location
    

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dept= models.ForeignKey(Department, on_delete= models.CASCADE, related_name="employees")
    salary = models.IntegerField(default=0)
    bouns = models.IntegerField(default=0)
    role= models.ForeignKey(Role, on_delete = models.CASCADE)
    phone= models.IntegerField(default=0000000000)
    hire_date= models.DateField()

    def __str__(self):
        return self.first_name + " " +self.last_name

