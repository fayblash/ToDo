from django.db import models
from accounts.models import Profile

# Create your models here.
class Goal(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=350, blank=True)
    target_date=models.DateField(null=True)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title