from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class UserType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    mobile= models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=8)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    user_type= models.ForeignKey(UserType,on_delete=models.CASCADE)

    
#class Report(models.Model):
# date = models.DateField()
# employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)

# def employee_id(models.Model):
#      title = models.CharField(max_length=50)
#     
#      def __str__(self):
#          return self.title