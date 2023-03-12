from django.db import models
from accounts.models import Profile

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    isDone = models.BooleanField(default=False)
    def __str__(self):
        return self.content[:20]

