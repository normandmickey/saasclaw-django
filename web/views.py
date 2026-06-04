from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import get_object_or_404, redirect, render
from .forms import HistoryLoadForm
from .models import HistoryLoad
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import TaskForm
from .models import Task


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

def _task_payload_to_form_data(payload, instance=None):
    return {
        'name': payload.get('name', instance.name if instance else ''),
    }


def _serialize_task(item):
    return {
        'id': item.pk,
        'name': item.name,
        'created_at': item.created_at.isoformat() if getattr(item, 'created_at', None) else '',
        'updated_at': item.updated_at.isoformat() if getattr(item, 'updated_at', None) else '',
    }


@login_required
def task_list(request):
    items = Task.objects.all()
    filter_definitions = []
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "task_list.html", {"form": form, "items": items, "filter_definitions": filter_definitions})


@login_required
def task_edit(request, pk):
    item = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=item)
    return render(request, "task_edit.html", {"form": form, "item": item})


@csrf_exempt
@login_required
def api_task_collection(request):
    if request.method == "GET":
        items = Task.objects.all()
        filter_definitions = []
        return JsonResponse({"items": [_serialize_task(item) for item in items]})
    if request.method == "POST":
        try:
            payload = json.loads(request.body.decode('utf-8') or '{}') if request.body else {}
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body."}, status=400)
        form = TaskForm(_task_payload_to_form_data(payload))
        if form.is_valid():
            item = form.save()
            return JsonResponse({"item": _serialize_task(item)}, status=201)
        return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
    return JsonResponse({"error": "Method not allowed."}, status=405)


@csrf_exempt
@login_required
def api_task_detail(request, pk):
    item = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return JsonResponse({"item": _serialize_task(item)})
    if request.method in {"POST", "PUT", "PATCH"}:
        try:
            payload = json.loads(request.body.decode('utf-8') or '{}') if request.body else {}
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body."}, status=400)
        form = TaskForm(_task_payload_to_form_data(payload, instance=item), instance=item)
        if form.is_valid():
            item = form.save()
            return JsonResponse({"item": _serialize_task(item)})
        return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
    if request.method == "DELETE":
        item.delete()
        return JsonResponse({"ok": True})
    return JsonResponse({"error": "Method not allowed."}, status=405)

