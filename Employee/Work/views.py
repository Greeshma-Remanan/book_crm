
from django.shortcuts import render
from django.views.generic import View
from Work.forms import EmpForm,EmpDeptForm,BookForm,LuminarForm,MarianForm,StudentsForm
from Work.models import Emp,EmpDept,Book,Luminar,Marian,Students
from django.shortcuts import redirect


# Create your views here.
class EmployeeView(View):
    def get(self,request):
        form=EmpForm()
        return render(request,'addemp.html',{"form":form})
    def post(self,request):
        form=EmpForm(request.POST)
        #print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            #modelnames.objects.create
            Emp.objects.create(**form.cleaned_data) #add data to models or db ,
            #form.cleaned_data is a dict and values in key value pair it cannot add to db so unpacking this using **form.cleaned data
            form=EmpForm()
            return render(request,'addemp.html',{'form':form})
        
        else:
            return render(request,'addemp.html',{'form':form})

class EMPdeptView(View):
    def get(self,request):
        form=EmpDeptForm()
        return render(request,'empdept.html',{'form':form})
    def post(self,request):
        form=EmpDeptForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            EmpDept.objects.create(**form.cleaned_data)
            form=EmpDeptForm()
            return render(request,'empdept.html',{'form':form})
        else:
            return render(request,'empdept.html',{'form':form})

class BookView(View):
    def get(self,request):
        form=BookForm()
        return render(request,'book.html',{'form':form})
    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():
            """print(form.cleaned_data)
            book=form.cleaned_data.get("title")
            print(book)
            Book.objects.create(**form.cleaned_data)""" #ORM query
            """name=Book.objects.fetchall()
            print(name)"""

            form.save() # form.save() method to add the data into db without using ORM query (only for modelform)
            print("Created")

            form=BookForm()

            return render(request,'book.html',{'form':form})
        else:
            return render(request,'book.html',{'form':form})



#display all data in another page

class Booklist(View):
    def get(self,request):
        data=Book.objects.all()
        return render(request,'booklist.html',{'data':data})


class LuminarView(View):
    def get(self,request):
        form=LuminarForm()
        return render(request,'luminar.html',{'form':form})
    def post(self,request):
        form=LuminarForm(request.POST)
        if form.is_valid():
          

            form.save() 
            print("Created")

            form=LuminarForm()

            return render(request,'luminar.html',{'form':form})
        else:
            return render(request,'luminar.html',{'form':form})


class Luminarlist(View):
    def get(self,request):
        data=Luminar.objects.all()
        return render(request,'luminarlist.html',{'data':data})



class Book_detailView(View):
    def get(self,request,*args,**kwargs): #self,request,args,kwargs all are parameter inside the def fun.but actually these are dictionary
        # id=5
        print(kwargs)
        #**kwargs provides with flexibility to use keyword aruguments in our program usimg its as parameter
        #we can eventually pass many arguments(request)
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        return render(request,'bookdetail.html',{'data':qs})


class MarianView(View):
    def get(self,request):
        form=MarianForm()
        return render(request,'marian.html',{'form':form})

    def post(self,request):
        form=MarianForm(request.POST)
        if form.is_valid():
            form.save()
            print("created")
            form=MarianForm()
            return render(request,'marian.html',{'form':form})
        else:
            return render(request,'marian.html',{'form':form})


class MarianList(View):
    def get(self,request):
        data=Luminar.objects.all()
        return render(request,'marianlist.html',{'data':data})


class StudentsView(View):
    def get(self,request):
        form=StudentsForm()
        return render(request,'students.html',{'form':form})
    
    def post(self,request):
        form=StudentsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Students.objects.create(**form.cleaned_data)
            form=StudentsForm()
            return render(request,'students.html',{'form':form})
        else:
            return render(request,'students.html',{'form':form})

class Studentlist(View):
    def get(self,request):
        data=Students.objects.all()
        return render(request,'stdlist.html',{'data':data})


class Students_detailView(View):
    def get(self,request,**kwargs):
        # id=5
        print(kwargs)
       
        id=kwargs.get("pk")
        qs=Students.objects.get(id=id)
        return render(request,'studentdetails.html',{'data':qs})
    
#delete  a book from book db

class Book_delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Book.objects.get(id=id).delete()
        return redirect('book-al')

class Student_delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Students.objects.get(id=id).delete()
        return redirect('std-al')