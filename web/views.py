from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import get_object_or_404, redirect, render
from .forms import HistoryLoadForm
from .models import HistoryLoad


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

@login_required
def history_load_list(request):
    items = HistoryLoad.objects.all()
    if request.method == "POST":
        form = HistoryLoadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("history_load_list")
    else:
        form = HistoryLoadForm()
    return render(request, "history_load_list.html", {"form": form, "items": items})


@login_required
def history_load_edit(request, pk):
    item = get_object_or_404(HistoryLoad, pk=pk)
    if request.method == "POST":
        form = HistoryLoadForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("history_load_list")
    else:
        form = HistoryLoadForm(instance=item)
    return render(request, "history_load_edit.html", {"form": form, "item": item})

