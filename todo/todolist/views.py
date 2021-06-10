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
from shopping.models import ShoppingItem
from shopping.forms import ShoppingForm
from goals.models import Goal
from goals.forms import GoalForm

# Create your views here.
@login_required
def index(request):
    user = request.user.profile 
    task_form=TaskForm()
    tasks = Task.objects.filter(profile=user)
    shop_form=ShoppingForm()
    shops=ShoppingItem.objects.filter(profile=user)  
    goal_form=GoalForm()
    goals=Goal.objects.filter(profile=user)  
    if request.method == "POST":
        if 'add_todo' in request.POST:
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                task = task_form.save(commit=False)
                task.profile = user
                task.save()
        if 'add_shop' in request.POST:
            shop_form = ShoppingForm(request.POST)
            if shop_form.is_valid():
                shop = shop_form.save(commit=False)
                shop.profile = user
                shop.save()
            return redirect("index")
        if 'add_goal' in request.POST:
            goal_form = GoalForm(request.POST)
            if goal_form.is_valid():
                goal = goal_form.save(commit=False)
                goal.profile = user
                goal.save()
            return redirect("index")
        
    return render(request, "index.html", {"task_form": task_form, "tasks": tasks,"shop_form":shop_form,"shops":shops,"goal_form":goal_form,"goals":goals})
   
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, 'todolist/update_task.html', {"task_edit_form": form})

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")