from django import forms
from .models import Employee
from .models import HistoryLoad
from .models import Task

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'title', 'department', 'hire_date', 'is_active']

class HistoryLoadForm(forms.ModelForm):
    class Meta:
        model = HistoryLoad
        fields = ['name', 'client_name', 'ytd_load']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']

