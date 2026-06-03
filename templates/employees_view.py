from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path


SESSION_KEY = "employees"


def employee_page(request):
    employees = request.session.get(SESSION_KEY, [])
    values = {"name": "", "address": ""}
    error = ""

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        address = request.POST.get("address", "").strip()
        values = {"name": name, "address": address}

        if not name or not address:
            error = "Both name and address are required."
        else:
            employees = [
                {"name": item.get("name", ""), "address": item.get("address", "")}
                for item in employees
            ]
            employees.append({"name": name, "address": address})
            request.session[SESSION_KEY] = employees
            return HttpResponseRedirect("/employees/")

    return render(
        request,
        "employees.html",
        {
            "employees": employees,
            "values": values,
            "error": error,
        },
    )


urlpatterns = [
    path("employees/", employee_page, name="employees"),
]
