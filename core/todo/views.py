from django.shortcuts import render
from todo.forms import TaskCreateForm
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from todo.models import Task
# Create your views here.
def createTask(request):
    if request.method == 'POST':
        form = TaskCreateForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = Profile.objects.get(user = request.user)
            form.save()
            return HttpResponse('Done!')
    return render(request, 'todo/task_creation.html', context={'form': TaskCreateForm})

def updateTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isDone = not task.isDone
    task.save()
    return HttpResponse(f"status changed to {task.isDone}")

def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    content = task.content
    task.delete()
    return HttpResponse(f"task '{content}' deleted")

def showTasks(request):
    tasks = Task.objects.filter(user = Profile.objects.get(user=request.user))
    return render(request,'todo/tasks.html', context={'tasks': tasks})