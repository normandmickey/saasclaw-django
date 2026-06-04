from django.contrib import admin
from .models import Employee
from .models import HistoryLoad

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'title']
    search_fields = ['name', 'email', 'phone', 'title', 'department']

@admin.register(HistoryLoad)
class HistoryLoadAdmin(admin.ModelAdmin):
    list_display = ['name', 'client_name', 'ytd_load']
    search_fields = ['name', 'client_name']

