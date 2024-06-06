from django.db import models

# Create your models here.
# one-to-one relationship

class Contact(models.Model):
    phone_no=models.CharField(max_length=20, unique=True)
    address=models.CharField(max_length=40)

    def __str__(self):
        return self.phone_no
    
class Department(models.Model):

    name=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name=models.CharField(max_length=50)
    contact=models.OneToOneField(Contact, on_delete=models.CASCADE)
 
        
        
    def __str__(self):
        return self.name
    
Course_Choice=(
    ('', 'Civil'),
    ('2', 'Mechanical'),
    ('3', 'Electrical')
)
    
class Student(models.Model):
    semester=models.CharField(max_length=20, choices=Course_Choice, default=1)
    def __str__(self):
        return self.semester

    
