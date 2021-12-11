from django.urls import path
from . import views
from .views import ProjectListView, ProjectDetailView, ProjectCreateView
from .views import TaskCreateView, TaskDetailView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path('', views.home, name= 'home-page'),
    path('task/new', TaskCreateView.as_view(), name= 'task-create'),
    path('task/<int:pk>', TaskDetailView.as_view(), name= 'task-detail'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name= 'task-delete'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name= 'task-update'),
    path('project/list', ProjectListView.as_view(), name= 'project-list'),
    path('project/new', ProjectCreateView.as_view(), name= 'project-create'),
    # path('project/<>', ProjectDetailView.as_view(), name= 'project-detail'),
]