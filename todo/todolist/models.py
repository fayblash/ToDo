from django.db import models
from accounts.models import Profile

# Create your models here.
class Task(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    title=models.CharField(max_length=350)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
