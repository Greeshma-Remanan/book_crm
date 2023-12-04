from django.db import models

# Create your models here.
#models: which is used to perform certain actions using data CRUD(create,read/write,update,delete)
 
class Employee(models.Model):
    uname=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)
    email=models.EmailField(null=True) #unique=true 

    def __str__(self):
        return self.uname  #return all name from the db

class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField(null=True)
    email=models.EmailField(unique=True,null=True) 
    place=models.CharField(max_length=30)
    #subject=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)

   
    def __str__(self):
        return self.name 
    
    # def __str__(self,name,age,email,place,gender):
    #     self.name = name
    #     self.age=age
    #     self.email=email
    #     self.place=place
    #     self.gender=gender
    #     return(self.name,self.age,self.email,self.place,self.gender)


#constraints: conditions for field


class Emp(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    salary=models.PositiveIntegerField()
    contact=models.CharField(max_length=30)


class EmpDept(models.Model):
    name=models.CharField(max_length=30)
    dept=models.CharField(max_length=30)
    salary=models.PositiveIntegerField()


class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    publication_year=models.CharField(max_length=20)
    genre=models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Luminar(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True,null=True)
    course=models.CharField(max_length=30)

class Marian(models.Model):
    name=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    hostel=models.CharField(max_length=30)


class Students(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    course=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    place=models.CharField(max_length=30)

