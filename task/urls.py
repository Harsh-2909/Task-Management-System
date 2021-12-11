from django.urls import path
from . import views
# from .views import ProjectListView
from .views import TaskCreateView, TaskDetailView, ProjectCreateView

urlpatterns = [
    path('', views.home, name= 'home-page'),
    path('task/new', views.TaskCreateView.as_view(), name= 'task-create' ),
    path('project/new', views.ProjectCreateView.as_view(), name= 'project-create' ),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name= 'task-detail' ),
    # path('projects/', ProjectListView.as_view(), name= 'project-list'),
]