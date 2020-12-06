"""URL patterns for todo list"""

from django.urls import path

from . import views

app_name = "todo_list"

urlpatterns = [
    path('', views.index, name="todo_list"),
    path('task_edit/<int:pk>/', views.task_edit, name="task_edit"),
    path('task_delete/<int:pk>/', views.task_delete, name="task_delete"),
]
