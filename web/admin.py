from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'title']
    search_fields = ['name', 'email', 'phone', 'title', 'department']

