from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from web.views import health, home
from web.views import employee_list
from web.views import history_load_edit
from web.views import history_load_list
from web.views import api_task_collection
from web.views import api_task_detail
from web.views import task_edit
from web.views import task_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("health/", health, name="health"),
    path("", home, name="home"),
    path("employees/", employee_list, name="employee_list"),
    path("history-loads/<int:pk>/edit/", history_load_edit, name="history_load_edit"),
    path("history-loads/", history_load_list, name="history_load_list"),
    path("api/tasks/<int:pk>/", api_task_detail, name="api_task_detail"),
    path("api/tasks/", api_task_collection, name="api_task_collection"),
    path("tasks/<int:pk>/edit/", task_edit, name="task_edit"),
    path("tasks/", task_list, name="task_list"),
]
