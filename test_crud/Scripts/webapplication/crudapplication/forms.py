from django import forms
from crudapplication.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        Model = Employee
        fields = "__all__"