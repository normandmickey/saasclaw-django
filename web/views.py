from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee


@login_required
def home(request):
    return render(request, "home.html", {"project_name": "saasclaw-django"})


def health(_request):
    return JsonResponse({"ok": True, "service": "saasclaw-django"})

@login_required
def employee_list(request):
    items = Employee.objects.all()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm()
    return render(request, "employee_list.html", {"form": form, "items": items})

