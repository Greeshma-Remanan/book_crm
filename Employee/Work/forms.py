from django import forms
#from models import Emp
from Work.models import Book,Luminar,Marian,Students

class EmpForm(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.IntegerField()
    contact=forms.CharField()

class EmpDeptForm(forms.Form):
    name=forms.CharField()
    dept=forms.CharField()
    salary=forms.IntegerField()

"""class BookForm(forms.Form):
    title=forms.CharField()
    author=forms.CharField()
    publication_year=forms.CharField()
    genre=forms.CharField()"""

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        
        #or 
        # fields=['title','author','publication_year','genre']

class LuminarForm(forms.ModelForm):
    class Meta:
        model=Luminar
        fields='__all__'

class MarianForm(forms.ModelForm):
    class Meta:
        model=Marian
        fields='__all__'

class StudentsForm(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'