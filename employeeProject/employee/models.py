from django.db import models

# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=150)
    designation=models.CharField(max_length=150)
    salary=models.IntegerField()

    def __str__(self):
        return self.name

#python manage.py migrate

#python manage.py makemigrations
#python manage.py migrate
#python manage.py shell

#creating details
#from employee.models import Employees
# emp=Employees(name='raju',designation='hr',salary=25000)
# emp.save()
# emp=Employees(name='ram',designation='developer',salary=23000)
# emp.save()
# emp=Employees(name='vivek',designation='testing',salary=22000)
# emp.save()

# fetch all name
#emps=Employees.objects.all()
#emps--- all emp nameswill be printed

# to fetch one name from the model by using get(id=1)
#emp=Employees.objects.get(id=1)
# print(emp.name)
#raju
# print(emp.salary)
#25000

#for taking values one by one
#emps=Employees.objects.all()
#for emp in emps:
#   print(emp.name)
#   print(emp.salary)

#to update the salary
#emp=Employees.objects.get(id=3)
# print(emp.salary)
# 22000

# to update
# emp.salary=27000
# emp.save()

#to view
# emp.salary
# 27000

