from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','username','password','confirm_password','emp_code','position','mobile','user_type')
        labels ={
            'fullname':'Full Name',
            'emp_code':'EMP Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['user_type'].empty_label = "Select"
        self.fields['emp_code'].required = True
