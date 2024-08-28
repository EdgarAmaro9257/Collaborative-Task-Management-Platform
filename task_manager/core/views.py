from django.shortcuts import render, get_object_or_404
from .models import Project, Task
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'core/index.html')

@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'core/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'core/project_detail.html', {'project': project})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'core/task_detail.html', {'task': task})

