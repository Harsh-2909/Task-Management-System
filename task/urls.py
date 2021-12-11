from django.urls import path
from . import views
# from .views import ProjectListView
from .views import TaskCreateView, TaskDetailView, ProjectCreateView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path('', views.home, name= 'home-page'),
    path('task/new', views.TaskCreateView.as_view(), name= 'task-create'),
    path('project/new', views.ProjectCreateView.as_view(), name= 'project-create'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name= 'task-detail'),
    path('task/<int:pk>/delete', views.TaskDeleteView.as_view(), name= 'task-delete'),
    path('task/<int:pk>/update', views.TaskUpdateView.as_view(), name= 'task-update'),
    # path('projects/', ProjectListView.as_view(), name= 'project-list'),
]