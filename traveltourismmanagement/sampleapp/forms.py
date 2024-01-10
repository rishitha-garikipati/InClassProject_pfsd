from django import forms

class EmployeeForm(forms.Form):
    emp_id = forms.IntegerField(label="Enter Employee ID:")
    emp_name=forms.CharField(label="Enter Employee Name:",max_length=50)
    emp_desig = forms.CharField(label="Enter Employee Designation:", max_length=50)