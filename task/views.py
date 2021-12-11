from django.http import request
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)

from task.models import Project, Task


# Create your views here.
def home(request):
    return render(request, 'task/home.html', {'title': 'Home'})
class TaskCreateView(CreateView, LoginRequiredMixin):
    model = Task
    fields = ['title', 'description', 'task_list', 'assigned_to']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskDetailView(DetailView, LoginRequiredMixin):
    model = Task

class ProjectCreateView(CreateView, LoginRequiredMixin):
    model = Project
    fields = ['name']

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['status']

    def form_valid(self, form):
        return super().form_valid(form)
    
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.created_by or self.request.user == task.assigned_to

class TaskDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Task
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.created_by

# @user_passes_test(lambda u: u.is_superuser)
# class ProjectListView(ListView):
#     model = Project
#     template_name = 'task/project_list.html'
#     context_object_name = 'projects'