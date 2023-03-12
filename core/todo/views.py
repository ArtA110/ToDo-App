from django.shortcuts import render
from todo.forms import TaskCreateForm
from accounts.models import Profile,User
from django.http import HttpResponse
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
