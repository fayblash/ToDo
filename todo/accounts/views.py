from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import *
from todolist.models import Task
from shopping.models import ShoppingItem
from goals.models import Goal


# Create your views here.

def register(request):
    form = ProfileCreationForm()
    if request.method == "POST":
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'there was a problem with your signup data, please try again')
    return render(request, 'registration/register.html', {'form': form})
    

# @login_required
# def dashboard(request):
#     user = request.user.profile
#     tasks = Task.objects.filter(profile=user)
#     shops = ShoppingItem.objects.filter(profile=user)
#     goals= Goal.objects.filter(profile=user)
#     return render(request, 'dashboard.html', {'profile': user,})
   