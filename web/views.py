from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render


@login_required
def home(request):
    return render(request, "home.html", {"project_name": "saasclaw-django"})


def health(_request):
    return JsonResponse({"ok": True, "service": "saasclaw-django"})
