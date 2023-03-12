from django.shortcuts import render
from todo.forms import TaskCreateForm
from accounts.models import Profile
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from todo.models import Task
# Create your views here.
@login_required
def createTask(request):
    if request.method == 'POST':
        form = TaskCreateForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = Profile.objects.get(user = request.user)
            form.save()
            return redirect("/todo/tasks/")
    return render(request, 'todo/task_creation.html', context={'form': TaskCreateForm})

@login_required
def updateTask(request, pk):
    profile = get_object_or_404(Profile, user=request.user)
    task = get_object_or_404(Task, pk=pk)
    if task.user == profile:
        task.isDone = not task.isDone
        task.save()
    return redirect("/todo/tasks/")

@login_required
def deleteTask(request, pk):
    profile = get_object_or_404(Profile, user=request.user)
    task = get_object_or_404(Task, pk=pk)
    if task.user == profile:
        task.delete()
    return redirect("/todo/tasks/")

@login_required
def showTasks(request):
    profile = get_object_or_404(Profile, user=request.user)
    tasks = Task.objects.filter(user = profile)
    return render(request,'todo/tasks.html', context={'tasks': tasks, 'profile': profile})