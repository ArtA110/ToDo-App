from django.forms import ModelForm
from todo.models import Task

class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['user']
