from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

date_time = datetime.now()
day = str(date_time.day)
month = str(date_time.month)
year = str(date_time.year)
day_month_year = day+month+year
class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class City(models.Model):
    name=models.TextField()
    description = models.TextField()
#TODO: Add the cityId to Employees Model
class Employees(models.Model):
    code = models.CharField(max_length=100,blank=True) 
    firstname = models.TextField() 
    middlename = models.TextField(blank=True,null= True) 
    lastname = models.TextField() 
    gender = models.TextField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.TextField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
    # today_registed = models.CharField(default=day_month_year, max_length=50)

    def __str__(self):
        return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '