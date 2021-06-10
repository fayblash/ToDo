from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from accounts.models import Profile
from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import *

   
def update_goal(request, pk):
    goal = Goal.objects.get(id=pk)
    form = GoalForm(instance=goal)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, 'goals/update_goal.html', {"goal_edit_form": form})

def delete_goal(request, pk):
    goal = Goal.objects.get(id=pk)
    goal.delete()
    return redirect("index")