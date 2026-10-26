from django.urls import path
from aplicacionTarea.views import (
    TaskListCreateView,
    TaskDetailView,
    AllTasksListView,
    TaskDeleteView,
    TaskUpdateView,
)

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/all/", AllTasksListView.as_view(), name="all-tasks-list"),
    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
]